"""Gateway to PostgreSQL."""

import aiopg


class PostgreSQL:
    """PostgreSQL database gateway."""

    def __init__(self, config, *, loop):
        """Initializer."""
        self._config = config
        self._loop = loop
        self._engine = None

    async def start(self, _):
        """Start gateway."""
        self._engine = await aiopg.sa.create_engine(
            database=self._config['database'],
            user=self._config['user'],
            password=self._config['password'],
            host=self._config['host'],
            port=self._config['port'],
            minsize=self._config['minsize'],
            maxsize=self._config['maxsize'],
            loop=self._loop)

    async def shutdown(self, _):
        """Stop gateway."""
        self._engine.close()
        await self._engine.wait_closed()
