import logging
from extractor.pmc_fetcher import fetch_pmc_xml, parse_figure_captions
from extractor.db_storage import save_paper_to_db
import logging
from extractor.pmc_fetcher import fetch_pmc_xml, parse_figure_captions
from extractor.db_storage import save_paper_to_d
logger = logging.getLogger(__name__)

def ingest_from_file(file_path):
    """
    Ingest PMCIDs from a file, fetch their figure captions, and save to DB.

    Args:
        file_path (str): Path to the file containing PMCIDs (one per line)

    Returns:
        dict: summary with 'success_count' and 'errors' list
    """
    success_count = 0
    errors = []

    logger.info(f"Starting ingestion from file: {file_path}")

    try:
        with open(file_path, "r") as f:
            ids = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        logger.error(f"Input file not found: {file_path}")
        raise

    logger.info(f"Found {len(ids)} PMCIDs in the file.")

    for pmc_id in ids:
        try:
            logger.debug(f"Processing PMC ID: {pmc_id}")
            xml = fetch_pmc_xml(pmc_id)
            data = parse_figure_captions(xml)
            save_paper_to_db(pmc_id, data)
            success_count += 1
            logger.info(f"Successfully ingested {pmc_id}")
        except Exception as e:
            logger.error(f"Error ingesting {pmc_id}: {e}")
            errors.append({'id': pmc_id, 'error': str(e)})

    logger.info(f"Ingestion complete: {success_count} successes, {len(errors)} errors")
    return {"success_count": success_count, "errors": errors}
