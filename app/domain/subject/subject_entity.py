from sqlalchemy import Column
from sqlalchemy.orm import Mapped
from sqlalchemy.types import Date, String

from trait.basic import BaseEntity, HasTimestamps


class Subject(BaseEntity[int], HasTimestamps):
    content: Mapped[str] = Column(String)
    date: Mapped[str] = Column(Date)
