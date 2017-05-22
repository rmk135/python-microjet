"""Core."""

import asyncio
import logging

import dependency_injector.containers as containers
import dependency_injector.providers as providers


class Core(containers.DeclarativeContainer):
    """Core component providers container."""

    config = providers.Configuration(name='config')

    logger = providers.Singleton(logging.getLogger, name='example')

    loop = providers.Singleton(asyncio.get_event_loop)
