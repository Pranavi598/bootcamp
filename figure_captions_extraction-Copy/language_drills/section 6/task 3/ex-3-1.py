from pydantic import BaseModel, Field

class User(BaseModel):
    email: str = Field(..., description="User's email address")

def main():
    user = User(email="alice@example.com")
    print(user)

if __name__ == "__main__":
    main()
