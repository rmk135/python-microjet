"""MicroJet services module."""

from microjet import core


class Base:
    """Base service."""

    def __init__(self, config):
        """Initializer."""
        self.config = config


class Provider(core.providers.Singleton):
    """Service provider."""

    provided_type = Base


class Catalog(core.catalogs.DeclarativeCatalog):
    """Service providers catalog."""

    provider_type = Provider

    @classmethod
    def init(cls, config):
        """Initializer services."""
        for name, provider in cls.providers.items():
            if name not in config:
                continue
            provider.kwargs += (core.injections.KwArg('config', config[name]),)


class Postgresql(Base):
    """Postgresql service."""


class Redis(Base):
    """Redis service."""


class Cassandra(Base):
    """Cassandra service."""


class Rabbitmq(Base):
    """Rabbitmq service."""
