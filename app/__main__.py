from core.fastapi import app  # noqa: F401
from handler import *  # noqa: F401, F403
from container import MainContainer

container = MainContainer()
container.wire(["handler"])
