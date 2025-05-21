# core.py

from abstraction_level_2.types import ProcessorFn


def to_uppercase(line: str) -> str:
    """Convert line to uppercase."""
    return line.upper()

def to_snakecase(line: str) -> str:
    """Convert line to snake_case."""
    return line.replace(" ", "_").lower()
