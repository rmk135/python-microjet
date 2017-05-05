"""Service providers container."""

import microjet.core.services as services

import example.gateways.pg
import example.gateways.redis
import example.gateways.s3

from .core import Core


class Services(services.Container):
    """Service providers container."""

    db = services.Provider(example.gateways.pg.PostgreSQL,
                           config=Core.config.pgsql,
                           loop=Core.loop)

    redis = services.Provider(example.gateways.redis.Redis,
                              config=Core.config.redis,
                              loop=Core.loop)

    s3 = services.Provider(example.gateways.s3.S3,
                           config=Core.config.s3,
                           loop=Core.loop)
