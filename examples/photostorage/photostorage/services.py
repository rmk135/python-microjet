"""Services container."""

from microjet.containers import Container
from microjet.providers import Singleton

from microjet.gateways import pg
from microjet.gateways import redis
from microjet.gateways import s3

from .core import Core


class Services(Container):
    """Service providers container."""

    database = Singleton(pg.PostgreSQL, config=Core.config.pgsql,
                         loop=Core.loop)

    redis = Singleton(redis.Redis, config=Core.config.redis, loop=Core.loop)

    s3 = Singleton(s3.S3, config=Core.config.s3, loop=Core.loop)
