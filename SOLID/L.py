# Liskov Substitution Principle (LSP)

# Below violation of the principle

class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height

    @property
    def area(self) -> int:
        return self._width * self._height

    def __repr__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.height})'

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        self._width = value

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        self._height = value


class Square(Rectangle):
    def __init__(self, size: int) -> None:
        super().__init__(size, size)

    @Rectangle.width.setter
    def width(self, value: int) -> None:
        self._width = value
        self._height = value

    @Rectangle.height.setter
    def height(self, value: int) -> None:
        self._width = value
        self._height = value


def use_it(rc: Rectangle) -> None:
    w = rc.width
    rc.height = 10
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rc.area}')


rc_1 = Rectangle(2, 3)
use_it(rc_1)
# Expected an area of 20, got 20

sq_1 = Square(5)
use_it(sq_1)
# Expected an area of 50, got 100
# bad ^
