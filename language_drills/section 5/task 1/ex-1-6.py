from collections import OrderedDict


def main():
    # Preserve order of insertion using OrderedDict
    od = OrderedDict()
    od['apple'] = 1
    od['banana'] = 2
    od['cherry'] = 3

    # Iterate over OrderedDict items
    for key, value in od.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
