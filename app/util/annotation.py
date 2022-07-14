from typing import TYPE_CHECKING, TypeVar

BaseType = TypeVar("BaseType", bound=type)


def mixin_base(type_: BaseType) -> BaseType:
    if TYPE_CHECKING:
        return type_
    else:
        return object
