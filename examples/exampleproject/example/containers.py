"""Application containers."""

import asyncio
import logging

import aiohttp.web

import dependency_injector.containers as containers
import dependency_injector.providers as providers

import microjet.gateways.pg
import microjet.gateways.redis
import microjet.gateways.s3

import example.models.users
import example.models.photos
import example.handlers.example


class Core(containers.DeclarativeContainer):
    """Core providers container."""

    config = providers.Configuration(name='config')

    logger = providers.Singleton(logging.getLogger, name='example')

    loop = providers.Singleton(asyncio.get_event_loop)


class Services(containers.DeclarativeContainer):
    """Service providers container."""

    db = providers.Singleton(microjet.gateways.pg.PostgreSQL,
                             config=Core.config.pgsql,
                             loop=Core.loop)

    redis = providers.Singleton(microjet.gateways.redis.Redis,
                                config=Core.config.redis,
                                loop=Core.loop)

    s3 = providers.Singleton(microjet.gateways.s3.S3,
                             config=Core.config.s3,
                             loop=Core.loop)


class Models(containers.DeclarativeContainer):
    """Model providers container."""

    # Photos
    photos_factory = providers.Factory(example.models.photos.Photo)

    photos_manager = providers.Singleton(
        example.models.photos.PhotosManager,
        photos_factory=photos_factory.delegate(),
        db=Services.db)

    # Users
    users_factory = providers.Factory(example.models.users.User)

    users_manager = providers.Singleton(
        example.models.users.UsersManager,
        users_factory=users_factory.delegate(),
        photos_manager=photos_manager,
        db=Services.db)


class WebHandlers(containers.DeclarativeContainer):
    """Web handler providers container."""

    handle = providers.Factory(example.handlers.example.example,
                               logger=Core.logger,
                               db=Services.db)


class Application(containers.DeclarativeContainer):
    """Application providers container."""

    app_factory = providers.Factory(aiohttp.web.Application,
                                    logger=Core.logger,
                                    debug=Core.config.debug)

    run_app = providers.Callable(aiohttp.web.run_app,
                                 host=Core.config.host,
                                 port=Core.config.port,
                                 loop=Core.loop)
