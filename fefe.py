class School:
    def __init__(self, name, students):
        self.name = name
        self.student = students
    def admit_student(self, student):
        self.students.append(student)
        print(f'{student.name} був доданий до {self.name}')
    def expel_student(self, student):
        expelled_student = next(filter(lambda s: s.name == student.name and s.grade == student.grade, self.students), None)
        if expelled_student is not None:
            self.students.remove(student)
            print(f'{expelled_student.name} був видалений з {self.name}')
        else:
            print(f'{student.name} не був знацдений в {self.name}') #або {expelled_student.name}
class Student:
        def __init__(self, name, grate):
            self.name = name
            self.grate = grate
        def promote(self):
            self.grate += 1
            print(f'{self.name} був підвищиниц {self.grade}')
        def demote(self):
            self.grate -= 1
            print(f'{self.name} був понижений {self.grade}')
        def __str__(self):
            return f'{self.name} - Ранг {self.grate}'

lisa =  Student('Alisa', 6)
masha = Student('Masha', 8)
andriy = Student('Andriy', 50)
dima = Student('Dmytro', 23)
gleb = Student('Gleb', 100)
my_school = School('ItStep', [lisa, masha, andriy, dima, gleb])


multiply = lambda x, y: x * y
print(multiply(8, 4))
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered_numbers)