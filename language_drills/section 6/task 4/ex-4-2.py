import logging

def main():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("LoggingLevels")

    logger.debug("This is a DEBUG message.")
    logger.info("This is an INFO message.")
    logger.warning("This is a WARNING message.")
    logger.error("This is an ERROR message.")

if __name__ == "__main__":
    main()
