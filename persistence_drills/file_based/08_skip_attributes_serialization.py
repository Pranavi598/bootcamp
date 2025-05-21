import json


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def to_json(self):
        """
        Convert the User object to a JSON string, skipping the password attribute.
        """
        # Create a dictionary of the object's attributes, excluding the password.
        user_data = {
            "username": self.username,
            "email": self.email
        }
        return json.dumps(user_data)

    @classmethod
    def from_json(cls, json_data):
        """
        Create a User object from a JSON string.
        """
        data = json.loads(json_data)
        return cls(data["username"], data["email"], None)  # Password is not in the JSON

    def __repr__(self):
        return f"User(username={self.username}, email={self.email})"


# Example usage:
def main():
    # Create a User instance
    user = User("alice", "alice@example.com", "secret_password")

    # Serialize the User object to JSON (password will be skipped)
    user_json = user.to_json()
    print("Serialized User (without password):", user_json)

    # Deserialize the JSON string back to a User object
    deserialized_user = User.from_json(user_json)
    print("Deserialized User object:", deserialized_user)


if __name__ == "__main__":
    main()
