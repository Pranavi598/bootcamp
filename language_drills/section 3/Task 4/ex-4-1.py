from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int = 0  # Default value for age


def main():
    user1 = User("Alice", 25)
    user2 = User("Bob")

    print(user1)
    print(user2)


if __name__ == "__main__":
    main()
