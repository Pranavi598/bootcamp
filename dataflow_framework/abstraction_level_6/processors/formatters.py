from typing import Iterator, Tuple

def snakecase(lines: Iterator[str]) -> Iterator[Tuple[str, str]]:
    for line in lines:
        transformed = line.lower().replace(" ", "_")
        print(f"[general -> snakecase]: {transformed}")
        yield "end", transformed
