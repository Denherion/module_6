from math import pi, sqrt

class Figure:
    sides_count = 0

    def __init__(self, color, *sides: int):
        self.__color = color
        self.__sides = sides
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int):
        if all in range(0, 255):
            return r, g, b

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        if self.sides_count == int(len(sides)) and self.sides_count > 0:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [*new_sides]

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = sides
        self.__radius = self.__sides[0] / (2 * pi)

    def get_square(self, color, *sides):
        __area = pi * (self.__radius ** 2)
        return __area

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides = sides

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return sqrt(p * (p - a) * (p - b) * (p - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides = sides
        self.set_sides(*[sides[0]] * self.sides_count)

    def get_volume(self):
        self.sides = self.get_sides()[0]
        return self.sides ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())