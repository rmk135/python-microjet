"""Services container."""

import microjet.containers as containers
import microjet.providers as providers

import microjet.gateways.pg
import microjet.gateways.redis
import microjet.gateways.s3

from .core import Core


class Services(containers.Container):
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
