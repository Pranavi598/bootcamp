from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    name: str
    age: int
    country: str = "India"


def main():
    user1 = User("Alice", 30)
    print(f"User: {user1.name}, Age: {user1.age}")

    try:
        user1.age = 35  # Trying to modify a frozen dataclass
    except AttributeError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
