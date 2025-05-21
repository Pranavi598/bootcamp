from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int = 0

    def is_adult(self):
        return self.age >= 18


def main():
    user1 = User("Alice", 25)
    user2 = User("Bob", 16)

    print(f"{user1.name} is an adult: {user1.is_adult()}")
    print(f"{user2.name} is an adult: {user2.is_adult()}")


if __name__ == "__main__":
    main()
