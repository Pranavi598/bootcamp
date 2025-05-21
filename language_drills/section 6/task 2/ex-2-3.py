from pydantic import BaseModel
from typing import Optional

class Profile(BaseModel):
    bio: str
    website: Optional[str] = None

class User(BaseModel):
    name: str
    age: int
    profile: Profile

def main():
    nested_data = {
        "name": "Alice",
        "age": 30,
        "profile": {
            "bio": "Software Developer",
            "website": "https://alice.dev"
        }
    }
    user = User(**nested_data)
    print(user)

if __name__ == "__main__":
    main()
