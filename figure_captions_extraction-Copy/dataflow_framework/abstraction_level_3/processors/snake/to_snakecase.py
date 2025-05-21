# processors/fan_in/to_snakecase.py

def to_snakecase(text: str) -> str:
    # Implementation of snakecase conversion
    return text.replace(" ", "_").lower()

