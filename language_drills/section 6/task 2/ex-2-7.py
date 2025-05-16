from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


def main():
    user = User(name="Alice", age=30)

    user_dict = user.dict()
    user_json = user.json()

    print(f"User as Dict: {user_dict}")
    print(f"User as JSON: {user_json}")


if __name__ == "__main__":
    main()
