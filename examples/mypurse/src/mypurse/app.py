"""MyPurse application."""

import asyncio
import logging
import string

import passlib.hash

from microjet.ioc import (ApplicationContainer, Configuration, Factory,
                          Singleton)
from microjet.gateways import pg

from .domain import models
from .domain import mappers
from .domain import services


class MyPurseApp(ApplicationContainer):
    """Application container."""

    # Core
    config = Configuration(name='config')
    logger = Singleton(logging.getLogger, name='example')
    loop = Singleton(asyncio.get_event_loop)

    # Gateways
    database = Singleton(pg.PostgreSQL, config=config.pgsql, loop=loop)

    # Profiles
    profile_model_factory = Factory(models.Profile)

    profile_password_hasher_factory = Factory(
        passlib.hash.scrypt.using,
        salt_size=32, rounds=16, block_size=8, parallelism=1)

    profile_password_generator_factory = Factory(
        models.RandomPasswordGenerator,
        password_length=8,
        characters=(string.ascii_lowercase + string.ascii_uppercase +
                    string.digits + string.punctuation))

    profile_mapper = Singleton(
        mappers.ProfileMapper,
        profile_model_factory=profile_model_factory.delegate(),
        database=database)

    # Services
    registration_service = Singleton(
        services.Registration,
        profile_model_factory=profile_model_factory.delegate(),
        profile_password_hasher=profile_password_hasher_factory,
        profile_mapper=profile_mapper)

    authentication_service = Singleton(
        services.Authentication,
        profile_password_hasher=profile_password_hasher_factory,
        profile_mapper=profile_mapper)

    password_update_service = Singleton(
        services.PasswordUpdate,
        profile_password_hasher=profile_password_hasher_factory,
        profile_password_generator=profile_password_generator_factory,
        profile_mapper=profile_mapper)
