from pydantic import BaseModel, conint, constr


class User(BaseModel):
    name: constr(min_length=3)
    age: conint(gt=0)


def main():
    try:
        valid_user = User(name="Alice", age=25)
        print(valid_user)

        invalid_user = User(name="Al", age=-5)  # Invalid name and age
    except ValidationError as e:
        print("Validation Error:", e)


if __name__ == "__main__":
    main()
