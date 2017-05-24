"""Core container."""

import asyncio
import logging

import microjet.containers as containers
import microjet.providers as providers


class Core(containers.Container):
    """Core component providers container."""

    config = providers.Configuration(name='config')

    logger = providers.Singleton(logging.getLogger, name='example')

    loop = providers.Singleton(asyncio.get_event_loop)
