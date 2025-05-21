import sys


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"'{self.title}' by {self.author}"

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class AudioMixin:
    def __init__(self, audio_format):
        self.audio_format = audio_format

    def play_audio(self):
        print(f"Playing {self.title} in {self.audio_format} format.")


class AudioBook(Book, AudioMixin):  # Multiple inheritance
    def __init__(self, title, author, audio_format):
        Book.__init__(self, title, author)
        AudioMixin.__init__(self, audio_format)


def main():
    if len(sys.argv) != 4:
        print("Usage: python book_program.py <title> <author> <audio_format>")
        sys.exit(1)

    title = sys.argv[1]
    author = sys.argv[2]
    audio_format = sys.argv[3]

    audiobook = AudioBook(title, author, audio_format)
    print(audiobook.describe())
    audiobook.play_audio()


if __name__ == "__main__":
    main()
