from typing import Any

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    create_async_engine,
)
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.sql import Delete, Insert, Update

from config import config

from .transactional import _dbsession_id


# Official SQLALCHEMY DOCS
# https://docs.sqlalchemy.org/en/14/orm/persistence_techniques.html#custom-vertical-partitioning
class PartitionedSession(Session):
    def get_bind(
        self,
        mapper: Any | None = ...,
        clause: Any | None = ...,
        bind: Any | None = ...,
        _sa_skip_events: Any | None = ...,
        _sa_skip_for_implicit_returning: bool = ...,
    ):
        if self._flushing or isinstance(clause, (Update, Delete, Insert)):
            return engines["write"].sync_engine
        else:
            return engines["read"].sync_engine


# https://docs.sqlalchemy.org/en/14/core/connections.html#schema-translating
engines = {
    "read": create_async_engine(
        config.READ_DB.SQLALCHEMY_URI,
        logging_name="Read",
        execution_options={"schema_translation_map": {None: config.READ_DB.SCHEMA}},
    ),
    "write": create_async_engine(
        config.WRITE_DB.SQLALCHEMY_URI,
        logging_name="Write",
        execution_options={"schema_translation_map": {None: config.WRITE_DB.SCHEMA}},
    ),
}

session_factory = sessionmaker(
    class_=AsyncSession, sync_session_class=PartitionedSession
)

session = async_scoped_session(
    session_factory=session_factory, scopefunc=_dbsession_id.get
)
