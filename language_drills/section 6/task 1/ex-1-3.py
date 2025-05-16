from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
    country: str = "India"

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative.")


def main():
    try:
        user1 = User("Alice", -1)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
