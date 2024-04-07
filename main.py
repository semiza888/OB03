# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется
# (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.

# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name  # Имя животного
        self.age = age  # Возраст животного

    def make_sound(self):
        return f"{self.name} is sound"

    def eat(self):
        return f"{self.name} is eating"

# Подкласс животных базового класса Animal
class Bird(Animal):
    def __init__(self, name, age, can_fly):
        super().__init__(name, age)
        self.can_fly = can_fly  # Может летать

    def make_sound(self):
        return f"{self.name} говорит 'Чирик-чирик!'"

    def eat(self):
        return f"{self.name} клюет зерна"

class Mammal(Animal):
    def __init__(self, name, age, has_fur):
        super().__init__(name, age)
        self.has_fur = has_fur  # Имеет шерсть

    def make_sound(self):
        return super().make_sound()

class Cat(Mammal):
    def __init__(self, name, age, has_fur=True):  # Все кошки имеющие шерсть по умолчанию
        super().__init__(name, age, has_fur)

    def make_sound(self):
        return f"{self.name} говорит 'Мяу-мяу!'"

    def eat(self):
        return f"{self.name} ест мясо"

class Reptile(Animal):
    def __init__(self, name, age, has_scales):
        super().__init__(name, age)
        self.has_scales = has_scales  # Имеют чешую на теле

    def make_sound(self):
        return f"{self.name} говорит 'Шшшшшш!'"

    def eat(self):
        return f"{self.name} ест мышей"

# Демонстрация полиморфизма
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

# Список животных разных видов
animals = [
    Bird("Чижик", 1, True),
    Cat("Васька", 5, True),
    Reptile("Гена", 4, True)
]

# Работы функции
animal_sound(animals)