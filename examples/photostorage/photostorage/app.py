"""PhotoStorage application."""

import asyncio
import logging

import passlib.hash

from microjet.ioc import (ApplicationContainer, Configuration, Factory,
                          Singleton)
from microjet.gateways import pg
from microjet.gateways import redis
from microjet.gateways import s3

from .domain import models
from .domain import mappers
from .domain import services


class PhotoStorage(ApplicationContainer):
    """Application container."""

    # Core
    config = Configuration(name='config')
    logger = Singleton(logging.getLogger, name='example')
    loop = Singleton(asyncio.get_event_loop)

    # Gateways
    database = Singleton(pg.PostgreSQL, config=config.pgsql, loop=loop)
    redis = Singleton(redis.Redis, config=config.redis, loop=loop)
    s3 = Singleton(s3.S3, config=config.s3, loop=loop)

    # Profiles
    profile_model_factory = Factory(models.Profile)

    profile_password_hasher_factory = Factory(
        passlib.hash.scrypt.using,
        salt_size=32, rounds=16, block_size=8, parallelism=1)

    profile_mapper = Singleton(
        mappers.ProfileMapper,
        profile_model_factory=profile_model_factory.delegate(),
        database=database)

    # Services
    profile_registration_service = Singleton(
        services.ProfileRegistrationService,
        profile_model_factory=profile_model_factory.delegate(),
        profile_password_hasher=profile_password_hasher_factory,
        profile_mapper=profile_mapper)
