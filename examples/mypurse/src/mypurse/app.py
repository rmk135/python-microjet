"""MyPurse application."""

import asyncio
import concurrent.futures
import logging

import passlib.hash

from microjet.ioc import (ApplicationContainer, Configuration, Factory,
                          Singleton)
from microjet.gateways import pg

from . import profile
from . import settings


class Core(ApplicationContainer):
    """Core container."""

    config = Configuration(name='config')
    logger = Singleton(logging.getLogger, name='example')
    loop = Singleton(asyncio.get_event_loop)
    thread_pool = Singleton(concurrent.futures.ThreadPoolExecutor,
                            max_workers=config.thread_pool_size)


class Gateways(ApplicationContainer):
    """Gatrways container."""

    database = Singleton(pg.PostgreSQL,
                         config=Core.config.pgsql, loop=Core.loop)


class Profile(ApplicationContainer):
    """Profile domain models container."""

    # Profile model
    profile_model_factory = Factory(
        profile.models.Profile,
        info=Factory(profile.models.ProfileInfo),
        password=Factory(profile.models.ProfilePassword),
        activation=Factory(profile.models.ProfileActivation))

    profile_mapper = Singleton(
        profile.mappers.ProfileMapper,
        profile_model_factory=profile_model_factory.delegate(),
        database=Gateways.database)

    # Profile info
    info_validator_factory = Factory(
        profile.models.ProfileInfoValidator,
        minimal_age_limit=settings.MINIMAL_AGE_LIMIT)

    # Profile password
    password_validator_factory = Factory(
        profile.models.ProfilePasswordValidator,
        minimal_length=settings.MINIMAL_PASSWORD_LENGTH)

    password_hasher_factory = Factory(
        profile.models.ProfilePasswordHasher,
        hasher=Factory(passlib.hash.scrypt.using,
                       salt_size=32, rounds=16, block_size=8, parallelism=1),
        thread_pool=Core.thread_pool,
        loop=Core.loop)

    # Profile activation
    activation_code_generator_factory = Factory(
        profile.models.ProfileActivationCodeGenerator,
        code_length=settings.ACTIVATION_CODE_LENGTH,
        code_characters=settings.ACTIVATION_CODE_CHARACTERS,
        code_ttl=settings.ACTIVATION_CODE_TTL)

    # Profile services
    registration_service = Singleton(
        profile.services.ProfileRegistration,
        profile_model_factory=profile_model_factory.delegate(),
        info_validator=info_validator_factory,
        activation_code_generator=activation_code_generator_factory,
        password_validator=password_validator_factory,
        password_hasher=password_hasher_factory,
        profile_mapper=profile_mapper)

    updater_service = Singleton(
        profile.services.ProfileUpdater,
        info_validator=info_validator_factory,
        password_validator=password_validator_factory,
        password_hasher=password_hasher_factory,
        profile_mapper=profile_mapper)
