import logging
import logging.config
import yaml
import os


CONFIG_FILEPATH = os.path.join(".", "logs", "config_logging.yaml")


def setup_logging(name=__name__):

    with open(CONFIG_FILEPATH, "r") as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)

    logger = logging.getLogger(name)
    return logger
