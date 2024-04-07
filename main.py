# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.

# Базовый класс Animal
class Animal:
    def __init__(self, name, age):

        self.name = name  # Имя животного
        self.age = age  # Возраст животного

    def make_sound(self):
        return f"{self.name} is sound"

    def eat(self):
        return f"{self.name} is eating"



