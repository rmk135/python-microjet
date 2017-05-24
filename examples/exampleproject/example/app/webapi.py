"""Web API container."""

import aiohttp

import dependency_injector.containers as containers
import dependency_injector.providers as providers

import example.webapi.example

from .core import Core
from .services import Services


class WebHandlers(containers.DeclarativeContainer):
    """Web handler providers container."""

    handle = providers.Factory(example.webapi.example.example,
                               logger=Core.logger,
                               db=Services.db)


class Application(containers.DeclarativeContainer):
    """Application providers container."""

    app_factory = providers.Factory(aiohttp.web.Application,
                                    logger=Core.logger,
                                    debug=Core.config.debug)

    run_app = providers.Callable(aiohttp.web.run_app,
                                 host=Core.config.host,
                                 port=Core.config.port,
                                 loop=Core.loop)
