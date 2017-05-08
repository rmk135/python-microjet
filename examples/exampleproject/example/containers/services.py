"""Service providers container."""

import dependency_injector.containers as containers
import dependency_injector.providers as providers

import example.gateways.pg
import example.gateways.redis
import example.gateways.s3

from .core import Core


class Services(containers.DeclarativeContainer):
    """Service providers container."""

    db = providers.Singleton(example.gateways.pg.PostgreSQL,
                             config=Core.config.pgsql,
                             loop=Core.loop)

    redis = providers.Singleton(example.gateways.redis.Redis,
                                config=Core.config.redis,
                                loop=Core.loop)

    s3 = providers.Singleton(example.gateways.s3.S3,
                             config=Core.config.s3,
                             loop=Core.loop)
