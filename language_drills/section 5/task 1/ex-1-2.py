from collections import Counter


def main():
    # Count character frequencies in "hello world"
    text = "hello world"
    char_count = Counter(text)

    # Print the character frequencies
    for char, count in char_count.items():
        print(f"'{char}': {count}")


if __name__ == "__main__":
    main()
