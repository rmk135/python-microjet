"""Core container."""

import asyncio
import logging

from microjet.containers import Container
from microjet.providers import Configuration, Singleton


class Core(Container):
    """Core component providers container."""

    config = Configuration(name='config')

    logger = Singleton(logging.getLogger, name='example')

    loop = Singleton(asyncio.get_event_loop)
