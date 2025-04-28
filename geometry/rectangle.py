from .base import Shape


class Rectangle(Shape):
    """Прямоугольник по ширине и высоте."""

    __slots__ = ("width", "height")

    def __init__(self, width: float, height: float) -> None:
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self.width = float(width)
        self.height = float(height)

    def area(self) -> float:
        return self.width * self.height

    def __repr__(self) -> str:  # pragma: no cover
        return f"Rectangle(width={self.width}, height={self.height})"
