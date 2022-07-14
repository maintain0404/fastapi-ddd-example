from logging.config import dictConfig

import yaml

LOGGING_CONFIG_FILE = "logging.yaml"


def configure_logging():
    with open(LOGGING_CONFIG_FILE) as f:
        config_dict = yaml.load(f.read(), yaml.FullLoader)
        dictConfig(config_dict)
