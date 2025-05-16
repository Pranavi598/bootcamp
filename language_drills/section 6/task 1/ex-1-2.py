from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    country: str = "India"  # Default country value

def main():
    user1 = User("Alice", 30)
    print(f"User: {user1.name}, Age: {user1.age}, Country: {user1.country}")

if __name__ == "__main__":
    main()
