def raise_stop_iteration():
    data = iter([1])
    try:
        print(next(data))
        print(next(data))  # Will raise StopIteration
    except StopIteration:
        print("Reached end of iterator")

if __name__ == "__main__":
    raise_stop_iteration()
