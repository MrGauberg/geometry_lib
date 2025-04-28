from abc import ABC, abstractmethod


class Shape(ABC):
    """Абстрактная геометрическая фигура."""

    @abstractmethod
    def area(self) -> float:  # pragma: no cover
        """Возвращает площадь фигуры."""
        ...  # pragma: no cover


def area(shape: "Shape") -> float:
    """
    Универсальная функция для получения площади без знания
    конкретного типа фигуры во время компиляции.
    """
    if not isinstance(shape, Shape):
        raise TypeError("Object must implement Shape interface")
    return shape.area()
