"""MicroJet models module."""

import dependency_injector.containers
import dependency_injector.providers


class Container(dependency_injector.containers.DeclarativeContainer):
    """Container of model providers."""


class Factory(dependency_injector.providers.Factory):
    """Model factory provider."""


class Singleton(dependency_injector.providers.Singleton):
    """Model singleton provider."""
