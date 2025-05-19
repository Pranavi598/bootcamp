from django.core.management.base import BaseCommand
from extractor.pmc_fetcher import fetch_pmc_xml, parse_figure_captions
from extractor.db_storage import save_paper_to_db

class Command(BaseCommand):
    help = 'Ingest PMCIDs from a file and store their figure data'

    def add_arguments(self, parser):
        parser.add_argument('--input', type=str, help='Path to input file containing PMCIDs')

    def handle(self, *args, **options):
        input_file = options['input']
        if not input_file:
            self.stderr.write("❌ No input file provided.")
            return

        try:
            with open(input_file, "r") as f:
                ids = [line.strip() for line in f if line.strip()]

            self.stdout.write(f"Ingesting {len(ids)} IDs from {input_file}…")

            success, errors = 0, []
            for pmc_id in ids:
                try:
                    xml = fetch_pmc_xml(pmc_id)
                    data = parse_figure_captions(xml)
                    save_paper_to_db(pmc_id, data)
                    success += 1
                except Exception as e:
                    errors.append({'id': pmc_id, 'error': str(e)})

            self.stdout.write(f"✅ Success: {success}")
            if errors:
                self.stderr.write(f"❌ Errors: {len(errors)}")
                for err in errors:
                    self.stderr.write(f"{err['id']}: {err['error']}")

        except FileNotFoundError:
            raise CommandError(f"File not found: {input_file}")
