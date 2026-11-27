"""ДЗ 9.1. Геометрична фігура "Ромб"

Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
- сторона_а (довжина сторони a).
- кут_а (кут між сторонами a і b).
- кут_б (суміжний з кутом кут_а).

Необхідно реалізувати наступні вимоги:
1. Значення сторони сторона_а повинно бути більше 0.
2. Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
3. Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а,
   значення кут_б обчислюється автоматично.
4. Для встановлення значень атрибутів використовуйте метод __setattr__.
"""


class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == "side_a" and value <= 0:
            raise ValueError("Error: side_a must be greater than 0")
        if key == "angle_a" and (value <= 0 or value >= 180):
            raise ValueError("angle_a must be between 0 and 180")
        if key == "angle_b":
            raise ValueError("angle_b is calculated automatically from angle_a")
        super().__setattr__(key, value)
        if key == "angle_a":
            super().__setattr__("angle_b", 180 - value)


rhombus = Rhombus(side_a=5, angle_a=60)
print(rhombus.__dict__)

try:
    Rhombus(side_a=0, angle_a=60)
except ValueError as error:
    print("Помилка:", error)
