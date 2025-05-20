# from django.core.management.base import BaseCommand, CommandError
# from extractor.pmc_fetcher import fetch_pmc_xml, parse_figure_captions
# from extractor.db_storage import save_paper_to_db
# import logging
#
# logger = logging.getLogger(__name__)
#
# class Command(BaseCommand):
#     help = 'Ingest PMCIDs from a file and store their figure data'
#
#     def add_arguments(self, parser):
#         parser.add_argument('--input', type=str, help='Path to input file containing PMCIDs')
#
#     def handle(self, *args, **options):
#         input_file = options['input']
#         if not input_file:
#             raise CommandError("❌ No input file provided. Use --input <file_path>")
#
#         try:
#             with open(input_file, "r") as f:
#                 ids = [line.strip() for line in f if line.strip()]
#
#             self.stdout.write(self.style.NOTICE(f"Ingesting {len(ids)} IDs from {input_file}…"))
#
#             success, errors = 0, []
#             for pmc_id in ids:
#                 try:
#                     xml = fetch_pmc_xml(pmc_id)
#                     data = parse_figure_captions(xml)
#                     save_paper_to_db(pmc_id, data)
#                     success += 1
#                 except Exception as e:
#                     error_msg = f"{pmc_id}: {e}"
#                     logger.error(error_msg)
#                     errors.append(error_msg)
#
#             self.stdout.write(self.style.SUCCESS(f"✅ Success: {success}"))
#             if errors:
#                 self.stderr.write(self.style.ERROR(f"❌ Errors: {len(errors)}"))
#                 for error in errors:
#                     self.stderr.write(error)
#
#         except FileNotFoundError:
#             raise CommandError(f"File not found: {input_file}")
from django.core.management.base import BaseCommand, CommandError
from extractor.pmc_fetcher import fetch_pmc_xml, parse_figure_captions
from extractor.db_storage import save_paper_to_db
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Ingest PMCIDs from a file and store their figure data'

    def add_arguments(self, parser):
        parser.add_argument('--input', type=str, help='Path to input file containing PMCIDs')

    def handle(self, *args, **options):
        input_file = options['input']
        if not input_file:
            raise CommandError("❌ No input file provided. Use --input <file_path>")

        try:
            with open(input_file, "r") as f:
                ids = [line.strip() for line in f if line.strip()]

            self.stdout.write(self.style.NOTICE(f"Ingesting {len(ids)} PMCIDs from {input_file}..."))
            logger.info(f"Starting ingestion of {len(ids)} PMCIDs from file {input_file}")

            success, errors = 0, []
            for pmc_id in ids:
                try:
                    xml = fetch_pmc_xml(pmc_id)
                    data = parse_figure_captions(xml)
                    save_paper_to_db(pmc_id, data)
                    success += 1
                    logger.info(f"Successfully ingested {pmc_id}")
                except Exception as e:
                    error_msg = f"{pmc_id}: {e}"
                    logger.error(error_msg)
                    errors.append(error_msg)

            self.stdout.write(self.style.SUCCESS(f"✅ Success: {success}"))
            if errors:
                self.stderr.write(self.style.ERROR(f"❌ Errors: {len(errors)}"))
                for error in errors:
                    self.stderr.write(error)

            logger.info(f"Ingestion complete: {success} successes, {len(errors)} errors")

        except FileNotFoundError:
            logger.error(f"File not found: {input_file}")
            raise CommandError(f"File not found: {input_file}")
