from datetime import datetime
from typing import ClassVar, Generic, Hashable, TypeVar

from provider.rdb import declarative_mixin, registry
from sqlalchemy import Column, MetaData, inspect
from sqlalchemy.orm import Mapped
from sqlalchemy.types import DateTime

EntityId = TypeVar("EntityId", bound=Hashable)


@registry.as_declarative_base()
class BaseEntity(Generic[EntityId]):
    metadata: ClassVar[MetaData]
    id: Mapped[EntityId]

    def _inspect_instance_state(self):
        state = inspect(self)
        if state.transient:
            return "transient"
        elif state.pending:
            return "pending"
        elif state.persistent:
            return "persistent"
        elif state.deleted:
            return "deleted"
        elif state.detached:
            return "detached"

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        prefix = f"{self.__class__.__name__}[{self._inspect_instance_state()}]"
        attr_info = ", ".join(
            [
                f"{key}={repr(getattr(self, key, 'UnsetOrUnload'))}"
                for key in inspect(self.__class___).attrs.keys()
            ]
        )
        return f"{prefix}({attr_info})"


@declarative_mixin
class HasTimestamps:
    created_at: Mapped[datetime] = Column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = Column(
        DateTime, default=datetime.now, onupdate=datetime.now
    )
