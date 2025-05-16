import sys


def main():
    large_list = [i for i in range(1000000)]
    large_gen = (i for i in range(1000000))

    print(f"List memory usage: {sys.getsizeof(large_list)} bytes")
    print(f"Generator memory usage: {sys.getsizeof(large_gen)} bytes")


if __name__ == "__main__":
    main()
