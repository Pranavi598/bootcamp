import logging

def main():
    logging.basicConfig(
        filename='logfile.log',
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s'
    )
    logger = logging.getLogger("FileLogger")
    logger.info("Logging to a file.")

if __name__ == "__main__":
    main()
