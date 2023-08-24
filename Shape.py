import math


class Shape:
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Create instances of shapes
side_of_square = float(input("Enter the side length of the square: "))
base_of_triangle = float(input("Enter the base length of the triangle: "))
height_of_triangle = float(input("Enter the height of the triangle: "))
radius_of_circle = float(input("Enter the radius of the circle: "))

square = Square(side_of_square)
triangle = Triangle(base_of_triangle, height_of_triangle)
circle = Circle(radius_of_circle)

# Calculate and display areas
print("Area of Square:", square.area())
print("Area of Triangle:", triangle.area())
print("Area of Circle:", circle.area())
