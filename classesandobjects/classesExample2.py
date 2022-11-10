import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_circumference(self):
        return 2 * math.pi * self.radius


circle1 = Circle(7)

print(type(circle1))

print(circle1.calculate_area())

print(circle1.calculate_circumference())
