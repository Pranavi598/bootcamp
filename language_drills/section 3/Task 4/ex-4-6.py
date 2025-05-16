from collections import namedtuple

# Define a Point with invalid field names
Point = namedtuple('Point', ['x coordinate', 'y coordinate'])

def main():
    point1 = Point(3, 4)
    print(f"Point coordinates: x={point1._1}, y={point1._2}")

if __name__ == "__main__":
    main()
