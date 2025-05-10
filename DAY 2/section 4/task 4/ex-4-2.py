import itertools


def main():
    # Cycle through a pattern and print 6 items
    color_cycle = itertools.cycle(["red", "green", "blue"])

    for _ in range(6):
        print(next(color_cycle))


if __name__ == "__main__":
    main()
