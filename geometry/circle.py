import math
from .base import Shape


class Circle(Shape):
    """Окружность по радиусу."""

    __slots__ = ("radius",)

    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = float(radius)

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def __repr__(self) -> str:  # pragma: no cover
        return f"Circle(radius={self.radius})"
