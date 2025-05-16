# multiple_contexts_example.py

def main():
    with open('file1.txt', 'w') as f1, open('file2.txt', 'w') as f2:
        f1.write("This is file 1.")
        f2.write("This is file 2.")

if __name__ == "__main__":
    main()
