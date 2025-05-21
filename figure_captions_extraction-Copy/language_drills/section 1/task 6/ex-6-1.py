def manual_iterator():
    items = [1, 2, 3]
    iterator = iter(items)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

if __name__ == "__main__":
    manual_iterator()
