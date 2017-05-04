"""MicroJet services module."""

import dependency_injector.containers
import dependency_injector.providers


class Container(dependency_injector.containers.DeclarativeContainer):
    """Container of service providers."""


class Provider(dependency_injector.providers.Singleton):
    """Service provider."""
