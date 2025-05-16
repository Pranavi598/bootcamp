from pydantic import BaseModel

class User(BaseModel):
    age: int

def main():
    user = User(age="42")  # Automatically converts string "42" to an integer
    print(user)

if __name__ == "__main__":
    main()
