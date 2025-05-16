from collections import deque

def main():
    # Rotate a deque by 2 positions and print the result
    d = deque([1, 2, 3, 4, 5])
    d.rotate(2)
    print(f"Deque after rotation: {d}")

if __name__ == "__main__":
    main()
