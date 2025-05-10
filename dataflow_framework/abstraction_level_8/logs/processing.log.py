import logging

logging.basicConfig(filename='logs/processing.log', level=logging.INFO)

logging.info(f"File {filename} started processing.")
logging.error(f"Error processing file {filename}: {error_message}")
