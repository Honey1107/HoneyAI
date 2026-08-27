# 13_Polymorphism
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def __str__(self):
        return f"{self.__class__.__name__}(area={self.area():.2f})"


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
        return 3.14159 * self.radius ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [Rectangle(4, 5), Circle(3), Triangle(6, 4)]

# Same method call, different behavior per object -- polymorphism
for shape in shapes:
    print(shape)

total_area = sum(shape.area() for shape in shapes)
print(f"Total area: {total_area:.2f}")

# Duck typing: no shared base class required, just the right method
class PaperShape:
    def area(self):
        return 42.0

for obj in shapes + [PaperShape()]:
    print(f"{type(obj).__name__} area via duck typing: {obj.area():.2f}")