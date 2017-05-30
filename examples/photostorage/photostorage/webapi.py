"""Web API container."""

import aiohttp

from microjet.containers import Container
from microjet.providers import Factory, Callable

from .app.webapi import example

from .core import Core
from .services import Services


class WebHandlers(Container):
    """Web handler providers container."""

    handle = Factory(example.example, logger=Core.logger,
                     db=Services.database)


class Application(Container):
    """Application providers container."""

    app_factory = Factory(aiohttp.web.Application, logger=Core.logger,
                          debug=Core.config.debug)

    run_app = Callable(aiohttp.web.run_app, host=Core.config.host,
                       port=Core.config.port, loop=Core.loop)
