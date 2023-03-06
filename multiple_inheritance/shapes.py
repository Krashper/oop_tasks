from math import pi
import abc

class Shape(abc.ABC):
    def area():
        raise NotImplementedError('Нельзя вызывать абстрактный метод')