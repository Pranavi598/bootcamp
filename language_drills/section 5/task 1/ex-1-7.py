from collections import defaultdict

def main():
    # Create a defaultdict with a lambda to return "N/A" for missing keys
    data = defaultdict(lambda: "N/A")
    data['name'] = 'John'
    print(f"Name: {data['name']}")
    print(f"Age: {data['age']}")  # Missing key, returns "N/A"

if __name__ == "__main__":
    main()
