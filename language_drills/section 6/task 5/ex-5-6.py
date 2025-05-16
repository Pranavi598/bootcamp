def fetch_data():
    return [1, 2, 3]

def double_values(data):
    return [x * 2 for x in data]

def main():
    raw = fetch_data()
    result = double_values(raw)
    print("Doubled values:", result)

if __name__ == "__main__":
    main()
