import logging

def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("NoPrint")

    # Replacing print
    logger.info("This replaces a print statement.")

if __name__ == "__main__":
    main()
