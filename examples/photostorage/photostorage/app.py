"""PhotoStorage application."""

import asyncio
import logging

import aiohttp

from microjet.containers import Container
from microjet.providers import Factory, Singleton, Callable, Configuration
from microjet.gateways import pg
from microjet.gateways import redis
from microjet.gateways import s3

from .bundles import profiles
from .bundles import auth
from .bundles import photos
from .webapi import example


class PhotoStorage(Container):
    """Application container."""

    # Core
    config = Configuration(name='config')
    logger = Singleton(logging.getLogger, name='example')
    loop = Singleton(asyncio.get_event_loop)

    # Services
    database = Singleton(pg.PostgreSQL, config=config.pgsql, loop=loop)
    redis = Singleton(redis.Redis, config=config.redis, loop=loop)
    s3 = Singleton(s3.S3, config=config.s3, loop=loop)

    # Profiles
    profile_models_factory = Factory(profiles.Profile)
    password_hashers_factory = Factory(profiles.PasswordHasher)
    profiles_manager = Singleton(
        profiles.ProfilesManager,
        profile_models_factory=profile_models_factory.delegate(),
        password_hasher=password_hashers_factory,
        database=database)

    # Auth
    auth_token_models_factory = Factory(auth.AuthToken)
    auth_manager = Singleton(
        auth.AuthManager,
        auth_token_models_factory=auth_token_models_factory.delegate(),
        database=database)

    # Photos
    photo_models_factory = Factory(photos.Photo)
    photos_manager = Singleton(
        photos.PhotosManager,
        photo_models_factory=photo_models_factory.delegate(),
        database=database)

    # Web API handlers
    web_handle = Factory(example.example, logger=logger, db=database)

    # Web API app
    web_app_factory = Factory(aiohttp.web.Application, logger=logger,
                              debug=config.debug)
    run_web_app = Callable(aiohttp.web.run_app, host=config.host,
                           port=config.port, loop=loop)
