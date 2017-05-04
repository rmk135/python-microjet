"""Example web handler."""

from aiohttp import web


async def example(request, *, logger, db):
    """Example request handler."""
    logger.info('Example request is handled')
    return web.Response(text='Hello, {name}!'.format(name='Roman'))
