from pydantic import BaseModel, Field


class User(BaseModel):
    """Represents a user in the system with a unique ID and email address."""

    id: int
    email: str = Field(..., description="User's email address")


def main():
    user = User(id=1, email="user@example.com")
    print(user)


if __name__ == "__main__":
    main()
