from collections import namedtuple

# Define a Point using namedtuple
Point = namedtuple('Point', ['x', 'y'])

def main():
    point1 = Point(3, 4)
    print(f"Point coordinates: x={point1.x}, y={point1.y}")

if __name__ == "__main__":
    main()
