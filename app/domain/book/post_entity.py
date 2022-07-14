from sqlalchemy import Column
from sqlalchemy.orm import Mapped
from sqlalchemy.types import String

from trait.basic import BaseEntity, HasTimestaps


class Book(BaseEntity, HasTimestaps):
    description: str[Mapped] = Column(String)
