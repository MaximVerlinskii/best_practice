# Open Close Principle (OCP)

from enum import Enum
from typing import Sequence, Generator


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(
        self,
        name: str,
        color: Color,
        size: Size
    ) -> None:
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(
        self,
        products: Sequence[Product],
        color: Color
    ) -> Generator[Product]:
        for p in products:
            if p.color == color:
                yield p
                