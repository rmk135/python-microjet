"""Services."""

import dependency_injector.containers as containers
import dependency_injector.providers as providers

import microjet.gateways.pg
import microjet.gateways.redis
import microjet.gateways.s3

from .core import Core


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
