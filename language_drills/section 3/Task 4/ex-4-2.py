from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    name: str
    age: int = 0


def main():
    user1 = User("Alice", 25)
    print(user1)

    try:
        user1.age = 30  # Attempting to modify a frozen dataclass should raise an error
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
