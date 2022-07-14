from typing import Callable, TypeVar

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import declarative_mixin as declarative_mixin_
from sqlalchemy.orm import declared_attr

from util.annotation import BaseType

PythonType = TypeVar("PythonType")


def queryable_declared_attr(t: Callable[..., PythonType]) -> Mapped[PythonType]:
    return declared_attr(t)


def declarative_mixin(type_: BaseType) -> BaseType:
    return declarative_mixin_(type_)
