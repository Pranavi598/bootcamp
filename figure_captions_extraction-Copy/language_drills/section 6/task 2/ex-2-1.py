from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

def main():
    user_data = {"name": "Alice", "age": 30}
    user = User(**user_data)
    print(user)

if __name__ == "__main__":
    main()
