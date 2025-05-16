from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int = 0  # Default value for age is 0

def main():
    # Creating a User object with both name and age provided
    user1 = User("Alice", 25)
    print(user1)  # Output: User(name='Alice', age=25)

    # Creating a User object with only name provided, age will default to 0
    user2 = User("Bob")
    print(user2)  # Output: User(name='Bob', age=0)

if __name__ == "__main__":
    main()
