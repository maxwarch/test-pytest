import math


class Shapes:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle:
    def __init__(self, radius: int | float) -> None:
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle:
    def __init__(self, width: int | float, height: int | float) -> None:
        self.width = width
        self.height = height
        self.is_square = True if width == height else False

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Rectangle):
            return False

        return self.width == value.width and self.height == value.height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return (self.width + self.height) * 2


class Square(Rectangle):
    def __init__(self, side: int | float) -> None:
        super().__init__(side, side)
