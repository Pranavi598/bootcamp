import itertools


def main():
    # Generate infinite IDs starting from 100
    id_generator = itertools.count(start=100)

    # Print the first 5 IDs
    for _ in range(5):
        print(next(id_generator))


if __name__ == "__main__":
    main()
