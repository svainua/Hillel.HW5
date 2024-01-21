#  Миколі потрібно перевірити, чи можливо із представлених відрізків умовної довжини сформувати трикутник.

# Для цього він вирішив створити клас TriangleChecker, який приймає лише позитивні числа.
# За допомогою методу is_triangle() повертаються такі значення (залежно від ситуації):
# (Потрібно згадати правило для трикутника та довжин його сторін)
# - Ура, можна побудувати трикутник!;
# - З негативними числами нічого не вийде!;
# - Потрібно вводити тільки числа!;
# – Жаль, але з цього трикутник не зробити.

# Створіть для Миколи класи  TriangleChecker, Triangle та класс ExtTriangle який від перших двух класів успадковує властивості
# - для перевірки створити обєкти трикутника з класу ExtTriangle та викликати метод is_triangle()  таким чином  щоб продемонструвати усі 4 можливі відповіді

# Triangle - відповідає за отримання значень сторін трикутника при створенні об'єкта.


class TriangleChecker:
    def is_triangle(self):
        if (
            type(self.side_1) == int
            and type(self.side_2) == int
            and type(self.side_3) == int
        ):
            if self.side_1 > 0 and self.side_2 > 0 and self.side_3 > 0:
                if (
                    (self.side_1 + self.side_2) <= self.side_3
                    or (self.side_1 + self.side_3) <= self.side_2
                    or (self.side_2 + self.side_3) <= self.side_1
                ):
                    return "Sorry you can not create a triangle using those sides"
                else:
                    return "Congrats! You can create a triangle!"
            else:
                return "There is nothing you can do with the negative number"
        else:
            return "You should enter only integers"


class Triangle:
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3


class ExtTriangle(Triangle, TriangleChecker):
    pass


triangle_1 = ExtTriangle(2, 2, 3)
print(triangle_1.is_triangle())

triangle_2 = ExtTriangle(2, 2, 5)
print(triangle_2.is_triangle())

triangle_3 = ExtTriangle(2, 2, -3)
print(triangle_3.is_triangle())

triangle_4 = ExtTriangle(2, 2, "d")
print(triangle_4.is_triangle())
