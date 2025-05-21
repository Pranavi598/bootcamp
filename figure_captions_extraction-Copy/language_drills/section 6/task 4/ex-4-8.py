import logging

def main():
    debug = True  # Toggle this to False to suppress debug messages
    level = logging.DEBUG if debug else logging.INFO

    logging.basicConfig(level=level)
    logger = logging.getLogger("ConditionalLogger")
    logger.debug("This debug message only shows if debug is True.")
    logger.info("This info message always shows.")

if __name__ == "__main__":
    main()
