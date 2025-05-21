from pydantic import BaseModel, validator

class User(BaseModel):
    name: str
    age: int

    @validator("name")
    def check_name_capitalization(cls, value):
        if not value[0].isupper():
            raise ValueError("Name must start with a capital letter")
        return value

def main():
    try:
        user1 = User(name="alice", age=25)  # Invalid name
    except ValidationError as e:
        print("Validation Error:", e)

if __name__ == "__main__":
    main()
