# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется
# (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных
# и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь
# специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

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
    Reptile("Каа", 4, True)
]

# Работа программы
animal_sound(animals)

# Класс сотрудника зоопарка

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position  # Должность сотрудника

# Класс ухаживающих за животными

class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name, position="Zoo Keeper")

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")

# Класс ветеринаров

class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, position="Veterinarian")

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")

# Класс Zoo, использующий композицию

class Zoo:
    def __init__(self):
        self.animals = []  # Пустой список животных в зоопарке
        self.employees = []  # Пустой список сотрудников зоопарка

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_animals(self):
        print("Животные в зоопарке:")
        for animal in self.animals:
            print(f"Имя: {animal.name}, Возраст: {animal.age}")

    def list_employees(self):
        print("Сотрудники зоопарка:")
        for employee in self.employees:
            print(f"Имя: {employee.name}, Должность: {employee.position}")

# Использование класса Zoo

zoo = Zoo()

# Добавление животных в зоопарк
zoo.add_animal(Bird("Чижик", 1, True))
zoo.add_animal(Cat("Васька", 5, True))
zoo.add_animal(Reptile("Каа", 4, True))

# Добавление сотрудников в зоопарк с использованием новых классов для каждой профессии
zoo.add_employee(ZooKeeper("Елена"))
zoo.add_employee(Veterinarian("Алексей"))

# Вывод информации о животных и сотрудниках зоопарка
zoo.list_animals()
zoo.list_employees()

# Работа программы
zoo.employees[0].feed_animal(zoo.animals[0])  # Елена кормит Чижика
zoo.employees[1].heal_animal(zoo.animals[1])  # Алексей лечит Ваську
