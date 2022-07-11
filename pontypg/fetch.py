import typing

import asyncpg  # type: ignore
from ponty import DoesNotExist

from pontypg.provider import lease_postgres_conn, defaultdb


async def fetchval(query: str, *a, dbname: str = defaultdb) -> typing.Any:
    async with lease_postgres_conn(dbname) as conn:
        return await conn.fetchval(query, *a)


async def fetchrow(query: str, *a, dbname: str = defaultdb) -> asyncpg.Record:
    async with lease_postgres_conn(dbname) as conn:
        record = await conn.fetchrow(query, *a)

    if not record:
        raise DoesNotExist

    return record


async def fetchrows(query: str, *a, dbname: str = defaultdb) -> list[asyncpg.Record]:
    async with lease_postgres_conn(dbname) as conn:
        return await conn.fetch(query, *a)




T = typing.TypeVar("T")


async def fetchone(query: str, *a, container: type[T], dbname: str = defaultdb) -> T:
    record = await fetchrow(query, *a, dbname=dbname)
    return container(**record)


async def fetchmany(query: str, *a, container: type[T], dbname: str = defaultdb) -> list[T]:
    records = await fetchrows(query, *a, dbname=dbname)
    return [container(**r) for r in records]
