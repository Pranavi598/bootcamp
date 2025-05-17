import json


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def to_json(self):
        # Convert to a dictionary and then to a JSON string
        return json.dumps({
            "title": self.title,
            "author": self.author,
            "pages": self.pages
        })

    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, pages={self.pages})"


def main():
    book = Book("The Alchemist", "Paulo Coelho", 208)

    json_data = book.to_json()
    print("Serialized Book object to JSON:")
    print(json_data)

    # Optionally save to a file
    with open("book.json", "w") as f:
        f.write(json_data)


if __name__ == "__main__":
    main()
