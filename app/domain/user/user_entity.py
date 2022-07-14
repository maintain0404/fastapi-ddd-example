from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from trait.basic import BaseEntity


class User(BaseEntity):
    idx = Column(Integer, primary_key=True)
    email = Column(String)
    name = Column(String)
    password = Column(String)
