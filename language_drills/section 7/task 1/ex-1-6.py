import time


def custom_sort(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


def main():
    import random
    data = [random.randint(0, 1000) for _ in range(1000)]

    start = time.time()
    sorted_builtin = sorted(data)
    print(f"Built-in sorted(): {time.time() - start:.6f} sec")

    start = time.time()
    sorted_custom = custom_sort(data.copy())
    print(f"Custom sort(): {time.time() - start:.6f} sec")


if __name__ == "__main__":
    main()
