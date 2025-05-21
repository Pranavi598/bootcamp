from dataclasses import dataclass

@dataclass(slots=True)
class User:
    name: str
    age: int
    country: str = "India"

def main():
    user1 = User("Alice", 30)
    print(f"User: {user1.name}, Age: {user1.age}, Country: {user1.country}")

    try:
        user1.city = "New York"  # Trying to add an attribute not defined in slots
    except AttributeError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
