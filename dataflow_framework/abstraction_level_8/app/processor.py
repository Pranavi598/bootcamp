from app.line_engine import run_stream  # Assume this exists

def process_file(file_path):
    with open(file_path, 'r') as f:
        run_stream(f)  # your Iterator[str] -> Iterator[str] pipeline



