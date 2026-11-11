"""One shared logging set-up for the whole pipeline.

Use this instead of print() inside src/. Log messages show the time, the
level (INFO, WARNING, ERROR) and which file wrote them, and they are saved to
logs/pipeline.log so we can look back at what happened in a run.

Example:
    from src.utils.logger import get_logger
    logger = get_logger(__name__)
    logger.info("Loaded 1,000 rows")
"""

import logging

from src.config import LOGS_DIR

# The layout of every log line: time | level | module | message
LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

# How the time is written, e.g. 2026-11-12 14:03:59
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# The file all log messages are written to.
LOG_FILE = LOGS_DIR / "pipeline.log"


def get_logger(name: str) -> logging.Logger:
    """Create (or reuse) a logger that writes to the console and to logs/pipeline.log.

    Args:
        name: The name shown in each log line. Pass __name__ so it shows the
            module that wrote the message, e.g. "src.etl.extract".

    Returns:
        A logging.Logger ready to use with .info(), .warning() and .error().
    """
    # Ask Python's logging module for a logger with this name. If one with the
    # same name already exists, Python gives us that same logger back.
    logger = logging.getLogger(name)

    # If this logger already has handlers, it was set up earlier. Adding them
    # again would print every message twice, so return it as it is.
    if logger.handlers:
        return logger

    # INFO and above are recorded (DEBUG messages are skipped).
    logger.setLevel(logging.INFO)

    # One formatter, shared by both outputs, so the console and the file look the same.
    formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)

    # Output 1: the console, so you can watch the pipeline while it runs.
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Output 2: the log file. Create logs/ first in case it does not exist yet
    # (for example on a fresh clone). mode="a" adds to the file instead of wiping it.
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    file_handler = logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Stop messages also being passed up to Python's root logger, which could
    # print them a second time in Jupyter notebooks.
    logger.propagate = False

    return logger
