from sqlalchemy import MetaData
from sqlalchemy.orm import registry as registry_

metadata = MetaData()
registry = registry_(metadata=metadata)
