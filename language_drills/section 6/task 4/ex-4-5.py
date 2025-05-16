import logging

def main():
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    logger = logging.getLogger("Formatter")
    logger.info("Formatted log message.")

if __name__ == "__main__":
    main()
