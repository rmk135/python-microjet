"""Services container."""

from microjet import containers
from microjet import providers

from microjet.gateways import pg
from microjet.gateways import redis
from microjet.gateways import s3

from .core import Core


class Services(containers.Container):
    """Service providers container."""

    db = providers.Singleton(pg.PostgreSQL,
                             config=Core.config.pgsql,
                             loop=Core.loop)

    redis = providers.Singleton(redis.Redis,
                                config=Core.config.redis,
                                loop=Core.loop)

    s3 = providers.Singleton(s3.S3,
                             config=Core.config.s3,
                             loop=Core.loop)
