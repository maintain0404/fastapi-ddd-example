from enum import Enum


class DeployMode(str, Enum):
    LOCAL = "local"
    DEVEVLOP = "dev"
    PRODUCTION = "prod"
    STAGE = "stage"
