from sqlalchemy import Column
from sqlalchemy.types import String

from app.provider.rdb import declarative_mixin, queryable_declared_attr


@declarative_mixin
class Explainable:
    @queryable_declared_attr
    def name(cls) -> str:
        return Column(
            String, nullable=False, comment=f'Name of entity "{cls.__name__}"'
        )

    @queryable_declared_attr
    def short_desc(cls) -> str:
        return Column(String, comment=f'Short description of entity "{cls.__name__}"')

    @queryable_declared_attr
    def long_desc(cls) -> str:
        return Column(String, comment=f'Long description of entity "{cls.__name__}"')
