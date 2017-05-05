"""Application component providers container."""

import aiohttp.web
import dependency_injector.containers as containers
import dependency_injector.providers as providers

from .core import Core


class Application(containers.DeclarativeContainer):
    """Application providers container."""

    app_factory = providers.Factory(aiohttp.web.Application,
                                    logger=Core.logger,
                                    debug=Core.config.debug)

    run_app = providers.Callable(aiohttp.web.run_app,
                                 host=Core.config.host,
                                 port=Core.config.port,
                                 loop=Core.loop)
