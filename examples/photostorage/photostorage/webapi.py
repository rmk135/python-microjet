"""Web API container."""

import aiohttp

from microjet import containers
from microjet import providers

from .app.webapi import example

from .core import Core
from .services import Services


class WebHandlers(containers.Container):
    """Web handler providers container."""

    handle = providers.Factory(example.example,
                               logger=Core.logger,
                               db=Services.db)


class Application(containers.Container):
    """Application providers container."""

    app_factory = providers.Factory(aiohttp.web.Application,
                                    logger=Core.logger,
                                    debug=Core.config.debug)

    run_app = providers.Callable(aiohttp.web.run_app,
                                 host=Core.config.host,
                                 port=Core.config.port,
                                 loop=Core.loop)
