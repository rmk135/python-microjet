"""Web handler providers container."""

import dependency_injector.containers as containers
import dependency_injector.providers as providers

import example.handlers.example

from .core import Core
from .services import Services


class WebHandlers(containers.DeclarativeContainer):
    """Web handler providers container."""

    handle = providers.Factory(example.handlers.example.example,
                               logger=Core.logger,
                               db=Services.db)
