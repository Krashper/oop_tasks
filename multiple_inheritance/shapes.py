from math import pi
import abc

class Shape(abc.ABC):
    @abc.abstractclassmethod
    def area():
        raise NotImplementedError('Нельзя вызывать абстрактный метод')
    @abc.abstractclassmethod
    def perimeter():
        raise NotImplementedError('Нельзя вызывать абстрактный метод')


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return (self.length + self.width) * 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return round(self.radius ** 2 * pi, 2)
    def perimeter(self):
        return round(2 * self.radius * pi, 2)