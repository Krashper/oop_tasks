from shapes import Circle, Rectangle


def test_class_circle():
    circle = Circle(2)
    assert circle.area() == 12.57
    assert circle.perimeter() == 12.57


def test_class_rectangle():
    rectangle = Rectangle(5, 4)
    assert rectangle.area() == 20
    assert rectangle.perimeter() == 18