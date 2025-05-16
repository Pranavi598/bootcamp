import logging

def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("SetupLogger")
    logger.info("Logger is set up successfully.")

if __name__ == "__main__":
    main()
