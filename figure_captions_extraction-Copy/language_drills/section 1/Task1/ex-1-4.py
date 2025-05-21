from collections import defaultdict


def dict_access(user):
    """
    Demonstrates .get() and .setdefault() with defaultdict.
    """
    name = user.get("name")  # Access using .get()
    user.setdefault("age", 25)  # Add 'age' key if it doesn't exist

    # Using defaultdict to demonstrate the concept
    user_default = defaultdict(lambda: "Unknown", user)

    return name, user, user_default


if __name__ == "__main__":
    # 4. Dictionary Access
    user = {"name": "Alice"}
    name, updated_user, user_default = dict_access(user)
    print(f"Name: {name}, Updated Dictionary: {updated_user}, DefaultDict: {user_default}")
