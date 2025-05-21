import pickle


class Person:
    def __init__(self, name, institutions, colleagues):
        self.name = name
        self.institutions = institutions
        self.colleagues = colleagues

    def __repr__(self):
        return f"Person(name={self.name}, institutions={self.institutions}, colleagues={self.colleagues})"


def main():
    with open("person.pkl", "rb") as f:
        person = pickle.load(f)

    print("Deserialized Person object:")
    print(person)


if __name__ == "__main__":
    main()
