from contextlib import asynccontextmanager
import typing

import asyncpg  # type: ignore
from ponty import Provider
from ponty.registry import Registry


_registry = Registry[asyncpg.pool.Pool]()
defaultdb: typing.Final[str] = "_default"


def postgres_provider(
    *,
    dbname: str = defaultdb,
    host: str,
    port: str = "5432",
    database: str,
    user: str,
    password: typing.Union[str, typing.Callable[[], str]] = "",
    min_size: int = 5,
    max_size: int = 20,
    command_timeout: typing.Optional[int] = 5,
) -> Provider:

    async def provider(_) -> typing.AsyncIterator[None]:
        pool = await asyncpg.create_pool(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password,
            min_size=min_size,
            max_size=max_size,
            command_timeout=command_timeout,
        )

        _registry.add(dbname, pool)

        try:
            yield
        finally:
            await pool.close()

    return provider


@asynccontextmanager
async def lease_postgres_conn(dbname: str = defaultdb) -> typing.AsyncIterator[asyncpg.Connection]:
    pool = _registry.get(dbname)
    async with pool.acquire() as conn:
        yield conn
