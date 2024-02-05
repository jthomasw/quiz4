class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private attribute

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._radius * 2

    def get_area(self):
        return 3.14 * self._radius * self._radius

def main():
    circle = Circle(5)

    print(f"Radius: {circle.get_radius()}")
    print(f"Diameter: {circle.get_diameter()}")
    print(f"Area: {circle.get_area()}")

if __name__ == '__main__':
    main()