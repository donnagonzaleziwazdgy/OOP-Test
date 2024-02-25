import math

class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class ShapeManager:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def total_area(self):
        total = 0
        for shape in self.shapes:
            if isinstance(shape, Shape):
                total += shape.area()
            else:
                print("Error: Only instances of Shape can be added to ShapeManager")
        return total


rectangle = Rectangle(5, 4)
circle = Circle(3)

shape_manager = ShapeManager()
shape_manager.add_shape(rectangle)
shape_manager.add_shape(circle)

print("Total area:", shape_manager.total_area())
