import pickle

class Person:
    def __init__(self, name):
        self.name = name
        self.friend = None  # This will hold a reference to another Person object

    def set_friend(self, friend):
        self.friend = friend

    def __repr__(self):
        return f"Person(name={self.name})"


# Create two Person objects that reference each other
alice = Person("Alice")
bob = Person("Bob")

# Establish cyclic references
alice.set_friend(bob)
bob.set_friend(alice)

# Serialize the objects with cyclic references using pickle
def serialize_with_cyclic_references():
    with open("cyclic_references.pkl", "wb") as file:
        pickle.dump(alice, file)

# Deserialize the objects and ensure the cyclic references are preserved
def deserialize_with_cyclic_references():
    with open("cyclic_references.pkl", "rb") as file:
        alice_restored = pickle.load(file)

    print(f"Restored Alice: {alice_restored}")
    print(f"Alice's friend: {alice_restored.friend}")
    print(f"Bob's friend: {alice_restored.friend.friend}")

# Run the serialization and deserialization
serialize_with_cyclic_references()
deserialize_with_cyclic_references()
