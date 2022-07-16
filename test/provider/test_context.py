import asyncio

import pytest
from provider.context import ctx


async def test_context():
    async def inner():
        ctx.type

    with ctx.inject(type="testtype"):
        await inner()


async def test_context_with_not_injected():
    async def inner():
        ctx.db_scope

    with pytest.raises(LookupError):
        with ctx.inject(type="testtype"):
            await inner()


async def test_context_multiple():
    async def inner(i):
        with ctx.inject(type=i):
            assert i == ctx.type

    await asyncio.gather(*(inner(i) for i in range(10)))


async def test_context_nested():
    with ctx.inject(type="testtype"):
        with ctx.inject(id="sdfsd"):
            ctx.type
            ctx.id
