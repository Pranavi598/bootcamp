from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    name: str
    age: int
    country: Optional[str] = None  # Nullable field with default of None


def main():
    user1 = User(name="Alice", age=30)
    print(f"User: {user1.name}, Country: {user1.country}")  # Country is None by default

    user2 = User(name="Bob", age=25, country="USA")
    print(f"User: {user2.name}, Country: {user2.country}")


if __name__ == "__main__":
    main()
