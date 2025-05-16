import logging
import os

# Setting up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def example_function():
    logger.debug("This is a debug message")
    logger.info("This is an info message")


def main():
    debug_mode = os.getenv('DEBUG', 'False') == 'True'

    if debug_mode:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.INFO)

    example_function()


if __name__ == "__main__":
    main()
