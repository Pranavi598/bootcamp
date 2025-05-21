from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(..., alias="user_id")

def main():
    input_data = {"user_id": 123}
    user = User(**input_data)
    print(user)

if __name__ == "__main__":
    main()
