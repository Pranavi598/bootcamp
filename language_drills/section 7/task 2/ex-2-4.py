def main():
    large_list = [i for i in range(1, 1000000)]
    if any(i % 99 == 0 for i in large_list):
        print("A number divisible by 99 exists!")
    else:
        print("No number divisible by 99 exists.")

if __name__ == "__main__":
    main()
