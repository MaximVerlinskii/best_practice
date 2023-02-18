# Open Close Principle (OCP)

from enum import Enum
from typing import Generator, Iterable, Any


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

# OCP = open for extension, closed for modification

# BAD
class ProductFilter:
    def filter_by_color(
        self,
        products: Iterable[Product],
        color: Color
    ) -> Generator[Product, None, None]:
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(
        self,
        products: Iterable[Product],
        size: Size
    ) -> Generator[Product, None, None]:
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(
        self,
        products: Iterable[Product],
        size: Size,
        color: Color
    ) -> Generator[Product, None, None]:
        for p in products:
            if p.color == color and p.size == size:
                yield p
# 2 -> 3 variants
# 3 -> 7 c s w cs sw cw csw


# GOOD
# Specification
class Specification:
    def is_satisfied(self, item: Any) -> bool:
        pass

    def __and__(self, other):
        # strange shit
        return AndSpecification(self, other)


class Filter:
    def filter(
        self,
        items: Iterable,
        spec: Specification
    ) -> Generator[Product, None, None]:
        pass


class ColorSpecification(Specification):
    def __init__(self, color: Color) -> None:
        self.color = color

    def is_satisfied(self, item: Any) -> bool:
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size: Size) -> None:
        self.size = size

    def is_satisfied(self, item: Any) -> bool:
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args) -> None:
        self.args = args

    def is_satisfied(self, item: Any) -> bool:
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


class BetterFilter(Filter):
    def filter(
        self,
        items: Iterable,
        spec: Specification
    ) -> Generator[Product, None, None]:
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    # BAD
    pf = ProductFilter()
    print('Green products (old):')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f' - {p.name} is green')

    # GOOD
    bf = BetterFilter()
    green_sf = ColorSpecification(Color.GREEN)
    print('Green products (new):')
    for p in bf.filter(products, green_sf):
        print(f' - {p.name} is green')

    print('Large products:')
    large_sf = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large_sf):
        print(f' - {p.name} is large')

    print('Large blue items:')
    # large_blue = AndSpecification(
    #     large_sf,
    #     ColorSpecification(Color.BLUE)
    # )
    large_blue = large_sf & ColorSpecification(Color.BLUE)
    for p in bf.filter(products, large_blue):
        print(f' - {p.name} is large and blue')
