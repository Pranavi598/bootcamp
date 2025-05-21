from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int = 0

@dataclass
class AdminUser(User):
    access_level: str

def main():
    admin = AdminUser("Alice", 30, "Admin")
    print(admin)
    print(f"Access Level: {admin.access_level}")

if __name__ == "__main__":
    main()
