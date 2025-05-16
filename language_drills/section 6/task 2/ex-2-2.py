from pydantic import BaseModel, ValidationError

class User(BaseModel):
    name: str
    age: int

def main():
    try:
        invalid_user = User(name="Bob", age="not a number")  # Invalid data type for age
    except ValidationError as e:
        print("Validation Error:", e)

if __name__ == "__main__":
    main()
