from typing import Generic, TypeVar

from sqlalchemy import select

from app.core.component import BaseRepo
from app.provider.rdb import session

from .basic_entity import BaseEntity, EntityId

Entity = TypeVar("Entity", bound=BaseEntity)


class BaseEntityRepo(BaseRepo, Generic[Entity]):
    __main_entity__: Entity

    async def get_only_by_id(self, id: EntityId) -> Entity | None:
        return session.scalar(
            select(self.__main_entity__).where(self.__main_entity__.id == id)
        )

    async def save(self, entity: Entity) -> None:
        await session.flush([entity])
