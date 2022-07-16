from contextvars import ContextVar, Token
from typing import TYPE_CHECKING, Generic, TypeVar
from uuid import UUID

if TYPE_CHECKING:
    from domain.user import User

else:
    User = None

ContextObj = TypeVar("ContextObj")


class ContextProperty(Generic[ContextObj]):
    def __set_name__(self, owner, name: str):
        self.name = name
        setattr(owner, f"_{name}", ContextVar(f"app_{name}"))

    def __get__(self, instance, cls) -> ContextObj:
        return getattr(instance, f"_{self.name}").get()


class _ContextExecutor:
    def __init__(self, *tokens: tuple[ContextVar, Token]):
        self.tokens = tokens

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        for ctx_var, token in self.tokens:
            ctx_var.reset(token)


class Context:
    type: ContextProperty[str] = ContextProperty()
    id: ContextProperty[UUID] = ContextProperty()
    user: ContextProperty[User] = ContextProperty()
    db_scope: ContextProperty[UUID] = ContextProperty()

    def inject(self, **kwargs) -> _ContextExecutor:
        tokens = []
        for name, value in kwargs.items():
            ctx_var: ContextVar = getattr(self, f"_{name}")
            token = ctx_var.set(value)
            tokens.append((ctx_var, token))

        return _ContextExecutor(*tokens)


ctx = Context()
