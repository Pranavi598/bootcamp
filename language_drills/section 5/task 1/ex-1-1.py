from collections import defaultdict


def main():
    # Group words by their first letter using defaultdict
    words = ['apple', 'banana', 'avocado', 'blueberry', 'cherry']
    grouped_words = defaultdict(list)

    for word in words:
        grouped_words[word[0]].append(word)

    # Print grouped words
    for key, value in grouped_words.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
