from functools import partial
from typing import Protocol


class AppException(Exception):
    msg: str
    internal_code: int
    status_code: int = 400

    def __init__(self, *, msg: str, status_code: int):
        self.msg = msg
        self.status_code = status_code

    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()


class MsgOnlyProtocol(Protocol):
    def __call__(self, *, msg: str) -> AppException:
        pass


EntityNotFound: MsgOnlyProtocol = partial(AppException, status_code=404)
