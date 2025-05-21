import pickle


class Person:
    def __init__(self, name, institutions, colleagues):
        self.name = name
        self.institutions = institutions  # list of strings
        self.colleagues = colleagues  # list of Person objects or names

    def __repr__(self):
        return f"Person(name={self.name}, institutions={self.institutions}, colleagues={self.colleagues})"


def main():
    alice = Person("Alice", ["IIT", "MIT"], ["Bob", "Charlie"])

    with open("person.pkl", "wb") as f:
        pickle.dump(alice, f)

    print("Person object serialized to person.pkl")


if __name__ == "__main__":
    main()
