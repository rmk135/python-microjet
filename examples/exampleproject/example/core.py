"""Core container."""

import asyncio
import logging

from microjet import containers
from microjet import providers


class Core(containers.Container):
    """Core component providers container."""

    config = providers.Configuration(name='config')

    logger = providers.Singleton(logging.getLogger, name='example')

    loop = providers.Singleton(asyncio.get_event_loop)
