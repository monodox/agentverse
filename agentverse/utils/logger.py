import logging


def get_logger(name: str = "agentverse") -> logging.Logger:
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(name)

