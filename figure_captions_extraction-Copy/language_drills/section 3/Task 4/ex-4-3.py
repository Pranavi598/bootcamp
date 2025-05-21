from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int = 0


def main():
    user1 = User("Alice", 25)
    user2 = User("Alice", 25)
    user3 = User("Bob", 30)

    print(user1 == user2)  # Should return True
    print(user1 == user3)  # Should return False


if __name__ == "__main__":
    main()
