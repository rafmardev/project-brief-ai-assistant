import logging
import sys

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    # Evitar agregar handlers duplicados
    if not logger.handlers:
        logger.addHandler(handler)

    uvicorn_loggers = (
        "uvicorn",
        "uvicorn.error",
        "uvicorn.access",
    )
    for logger_name in uvicorn_loggers:
        logging.getLogger(logger_name).handlers = []
        logging.getLogger(logger_name).propagate = True
    
    return logger