from enum import Enum

class Color(Enum):
    GREEN = 1
    RED = 2
    BLUE = 3
    YELLOW = 4

class Size(Enum):
    LARGE = 1
    MEDIUM = 2
    SMALL = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

class Specification:
    def is_satisfied(self, item):
        pass

    #def __and__(self, other):
    #    return AndSpecification(self, other)

class Filter:
    def filter(self, item, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class AndSpecification(Specification):
    def __init__(self, spec1, spec2):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_statisfied(self, item):
        return self.spec1.is_statisfied(item) and self.spec2.is_statisfied(item)

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

apple = Product('Apple', Color.GREEN, Size.LARGE)
samsung = Product('Samsung', Color.BLUE, Size.SMALL)
lenova = Product("Lenova", Color.GREEN, Size.SMALL)

products = [apple, samsung, lenova]


bf = BetterFilter()

green = ColorSpecification(Color.GREEN)
large = SizeSpecification(Size.LARGE)
blue = ColorSpecification(Color.BLUE)

print("Green products")
for p in bf.filter(products, green):
    print(f'-{p.name} is green')

print("---------Large product")

for p in bf.filter(products, large):
    print(f'-{p.name} is large')


print("----------Both large and green color ")
large_green = AndSpecification(large, green)

for p in bf.filter(products, large_green):
    print(f'-{p.name} large and gree')


print("------------Both large and Blue color")
large_blue = AndSpecification(large, blue)

for p in bf.filter(products, large_blue):
    print(f'-{p.name}')
