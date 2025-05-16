import logging

def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info(f"Logger name is: {logger.name}")

if __name__ == "__main__":
    main()
