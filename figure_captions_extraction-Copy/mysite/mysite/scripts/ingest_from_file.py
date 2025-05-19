import sys
from extractor.tasks import ingest_from_file

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ingest_from_file.py ids.txt")
        sys.exit(1)

    ingest_from_file(sys.argv[1])
