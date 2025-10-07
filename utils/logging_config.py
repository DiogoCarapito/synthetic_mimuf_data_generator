import colorlog


def logging_setup():
    handler = colorlog.StreamHandler()
    handler.setFormatter(
        colorlog.ColoredFormatter(
            "%(log_color)s%(levelname)s:%(reset)s %(message)s",
            log_colors={
                "DEBUG": "blue",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bold_red",
            },
        )
    )
    logger = colorlog.getLogger()
    logger.handlers = []  # Remove any existing handlers
    logger.addHandler(handler)
    logger.setLevel("INFO")
    return logger
