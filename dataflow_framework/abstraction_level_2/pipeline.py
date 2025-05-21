# pipeline.py

from abstraction_level_2.core import to_uppercase, to_snakecase
from abstraction_level_2.types import ProcessorFn

def build_pipeline(mode: str) -> list[ProcessorFn]:
    """Build the pipeline based on the mode."""
    if mode == "uppercase":
        return [to_uppercase]
    elif mode == "snakecase":
        return [to_snakecase]
    else:
        raise ValueError(f"Unsupported mode: {mode}")
