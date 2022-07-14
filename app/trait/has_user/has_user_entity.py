from sqlalchemy import Column
from sqlalchemy.orm import Mapped, declarative_mixin, declared_attr, relationship
from sqlalchemy.types import Integer


@declarative_mixin
class HasUser:
    user_id: Mapped[int] = Column(Integer)

    @declared_attr
    def user(cls):
        from app.domain.user import User

        return relationship(User, cls.user_id == User.idx)
