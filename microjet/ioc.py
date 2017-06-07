"""Application Inversion of Control container and providers.

This module provides  IoC container and its providers: Factory, Singleton,
Callable and Configuration.

IoC container and its providers are integrated from Dependency Injector
microframework.
"""

from dependency_injector import containers
from dependency_injector import providers


ApplicationContainer = containers.DeclarativeContainer

Configuration = providers.Configuration
Callable = providers.Callable
Factory = providers.Factory
Singleton = providers.Singleton
