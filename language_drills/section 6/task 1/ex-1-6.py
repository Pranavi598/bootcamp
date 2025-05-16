from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
    name: str
    age: int
    country: str = "India"
    tags: List[str] = field(default_factory=list)  # Factory for default list

def main():
    user1 = User("Alice", 30)
    print(f"User: {user1.name}, Tags: {user1.tags}")

if __name__ == "__main__":
    main()
