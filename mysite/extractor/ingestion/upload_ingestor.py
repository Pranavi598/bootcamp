import logging
from extractor.pmc_fetcher import fetch_pmc_xml, parse_figure_captions
from extractor.db_storage import save_paper_to_db

logger = logging.getLogger(__name__)

def ingest_from_uploaded_file(uploaded_file):
    """
    Ingest PMCIDs from an uploaded file-like object, fetch their figure captions, and save to DB.

    Args:
        uploaded_file (file-like): Uploaded file object containing PMCIDs (one per line)

    Returns:
        dict: summary with 'success_count' and 'errors' list
    """
    success_count = 0
    errors = []

    logger.info("Starting ingestion from uploaded file")

    # Read lines from uploaded file; decode bytes to string if needed
    lines = uploaded_file.read().decode('utf-8').splitlines()
    ids = [line.strip() for line in lines if line.strip()]

    logger.info(f"Found {len(ids)} PMCIDs in the uploaded file.")

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
