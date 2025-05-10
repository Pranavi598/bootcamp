# core.py

from typing import List
from abstraction_level_3.types import ProcessorFn

def process_lines(lines: List[str], processors: List[ProcessorFn]) -> List[str]:
    result = []
    for line in lines:
        for processor in processors:
            line = processor(line.strip())  # Apply each processor function to each line
        result.append(line)
    return result
