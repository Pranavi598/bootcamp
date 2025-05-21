from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    country: str = "India"

    def is_adult(self) -> bool:
        return self.age >= 18

def main():
    user1 = User("Alice", 30)
    print(f"Is {user1.name} an adult? {user1.is_adult()}")

if __name__ == "__main__":
    main()
