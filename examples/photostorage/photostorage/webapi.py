"""Web API."""

from aiohttp import web


async def example_hander(request, *, logger, db):
    """Example request handler."""
    logger.info('Example request is handled')
    return web.Response(text='Hello, {name}!'.format(name='Roman'))
