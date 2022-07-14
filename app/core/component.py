from typing import ClassVar
from logging import Logger, getLogger


class Component:
    logger: ClassVar[Logger]
    component_type: ClassVar[str]
    abstract: bool | None

    def __init_subclass__(cls) -> None:
        if not cls.abstract:
            cls.logger = getLogger(f"app.{cls.component_type}.{cls.__name__}")
        else:
            delattr(cls, "abstract")


class BaseService(Component):
    abstract: bool | None = True


class BaseUseCase(Component):
    abstract: bool | None = True


class BaseRepo(Component):
    abstract: bool | None = True
