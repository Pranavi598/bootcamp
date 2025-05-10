# zip_example.py

def main():
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']

    for item1, item2 in zip(list1, list2):
        print(f"{item1} - {item2}")


if __name__ == "__main__":
    main()
