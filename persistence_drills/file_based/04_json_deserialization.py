import json

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        return cls(data["title"], data["author"], data["pages"])

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, pages={self.pages})"


def main():
    with open("book.json", "r") as f:
        json_string = f.read()

    book = Book.from_json(json_string)
    print("Deserialized JSON to Book object:")
    print(book)

if __name__ == "__main__":
    main()
