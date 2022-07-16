from functools import wraps
from typing import Callable, ParamSpec, TypeVar
from uuid import uuid4

from provider.context import ctx

FuncParams = ParamSpec("FuncParams")
FuncReturn = TypeVar("FuncReturn")


def transactional():
    def decorator(
        func: Callable[FuncParams, FuncReturn]
    ) -> Callable[FuncParams, FuncReturn]:
        @wraps(func)
        async def _wrapped(
            *args: FuncParams.args, **kwargs: FuncParams.kwargs
        ) -> FuncReturn:
            with ctx.inject(db_scope=uuid4()):
                ret = await func(*args, **kwargs)
            return ret

    return decorator
