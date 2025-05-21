import sys


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"'{self.title}' by {self.author}"

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class Novel(Book):  # Subclassing Book
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre


def main():
    if len(sys.argv) != 4:
        print("Usage: python book_program.py <title> <author> <genre>")
        sys.exit(1)

    title = sys.argv[1]
    author = sys.argv[2]
    genre = sys.argv[3]

    novel = Novel(title, author, genre)
    print(f"Created Novel: {novel.title}, {novel.author}, Genre: {novel.genre}")


if __name__ == "__main__":
    main()
