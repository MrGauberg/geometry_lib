import math
from geometry.rectangle import Rectangle
import pytest
from geometry import Circle, Triangle, area


def test_circle_area():
    c = Circle(1)
    assert math.isclose(c.area(), math.pi)


def test_circle_invalid():
    with pytest.raises(ValueError):
        Circle(0)


def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6.0)


def test_triangle_invalid():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)


def test_triangle_right():
    assert Triangle(3, 4, 5).is_right()
    assert not Triangle(2, 3, 4).is_right()


def test_generic_area():
    figures = [Circle(2), Triangle(3, 4, 5)]
    areas = [area(f) for f in figures]
    assert math.isclose(areas[0], math.pi * 4)
    assert math.isclose(areas[1], 6.0)


def test_extensibility_error():
    class BadShape:
        def area(self):
            return 1

    with pytest.raises(TypeError):
        area(BadShape())


def test_rectangle_area():
    r = Rectangle(3, 7)
    assert r.area() == 21

def test_rectangle_invalid():
    with pytest.raises(ValueError):
        Rectangle(0, 5)