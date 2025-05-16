def generate_numbers():
    for i in range(1, 11):
        yield i

def main():
    for num in generate_numbers():
        print(num)

if __name__ == "__main__":
    main()
