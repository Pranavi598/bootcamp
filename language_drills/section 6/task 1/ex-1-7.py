from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    country: str = "India"

def main():
    user1 = User("Alice", 30)
    user2 = User("Alice", 30)
    user3 = User("Bob", 25)

    print(f"Are user1 and user2 equal? {user1 == user2}")
    print(f"Are user1 and user3 equal? {user1 == user3}")

if __name__ == "__main__":
    main()
