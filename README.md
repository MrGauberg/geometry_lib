# geometry-lib

Библиотека для вычисления площадей базовых геометрических фигур.

## Пример использования

```python
from geometry import Circle, Triangle, area

print(area(Circle(2)))         # 12.566370614359172
t = Triangle(3, 4, 5)
print(t.area())                # 6.0
print(t.is_right())            # True
```

## Установка и запуск тестов

Рекомендуется работать в изолированной виртуальной среде.

```bash
# Создаём и активируем виртуальную среду (Linux / macOS)
python3 -m venv venv
source venv/bin/activate

# Для Windows
python -m venv venv
.\venv\Scripts\activate

# Устанавливаем библиотеку в editable‑режиме и зависимости для тестов
pip install -e .
pip install pytest

# Запускаем тесты
pytest
```
