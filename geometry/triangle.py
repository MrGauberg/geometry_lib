import math
from .base import Shape


class Triangle(Shape):
    """Треугольник по трём сторонам."""

    __slots__ = ("a", "b", "c")

    def __init__(self, a: float, b: float, c: float) -> None:
        sides = sorted((a, b, c))
        if any(s <= 0 for s in sides):
            raise ValueError("Sides must be positive")
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Sides violate triangle inequality")
        self.a, self.b, self.c = map(float, (a, b, c))

    def area(self) -> float:
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right(self, tol: float = 1e-9) -> bool:
        """Проверка, прямоугольный ли треугольник (по теореме Пифагора)."""
        sides = sorted((self.a, self.b, self.c))
        return abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) <= tol

    def __repr__(self) -> str:  # pragma: no cover
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"
