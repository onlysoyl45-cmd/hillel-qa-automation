"""ДЗ 8.1. Об'єктний студент

Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу
"Студент", який дозволяє змінювати середній бал студента. Виведіть інформацію
про студента та змініть його середній бал.
"""


class Student:
    def __init__(self, first_name: str, last_name: str, age: int, average_grade: float):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def change_average_grade(self, new_grade):
        """Змінює середній бал студента на new_grade."""
        self.average_grade = new_grade

    def get_info(self) -> str:
        return f"Студент: {self.first_name} {self.last_name}, вік: {self.age}, середній бал: {self.average_grade}"


student = Student(first_name="Stepan", last_name="Bandera", age=20, average_grade=4.2)
print(student.get_info())
student.change_average_grade(4.8)
print(student.get_info())
