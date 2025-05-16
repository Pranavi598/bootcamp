from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., title="Full Name", example="Alice Smith")

def main():
    user = User(name="Alice Smith")
    print(user)

if __name__ == "__main__":
    main()
