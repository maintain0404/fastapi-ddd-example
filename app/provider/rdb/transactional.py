from functools import wraps
from uuid import uuid4
from contextvars import ContextVar
from typing import Callable, ParamSpec, TypeVar

FuncParams = ParamSpec("FuncParams")
FuncReturn = TypeVar("FuncReturn")
_dbsession_id: ContextVar[str] = ContextVar("_dbsession_id")


def transactional():
    def decorator(
        func: Callable[FuncParams, FuncReturn]
    ) -> Callable[FuncParams, FuncReturn]:
        @wraps(func)
        async def _wrapped(
            *args: FuncParams.args, **kwargs: FuncParams.kwargs
        ) -> FuncReturn:
            token = _dbsession_id.set(uuid4())
            ret = await func(*args, **kwargs)
            _dbsession_id.reset(token)
            return ret

    return decorator
