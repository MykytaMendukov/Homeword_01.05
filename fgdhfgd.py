class student:
    print('hi!')
    count = 0
    def __init__(self, height = 150):
        self.height = height
        student.count += 1
    def breathing(self):
        return self.height - 10
oleg = student()
print(oleg.height)
masha = student(height=200)
print(masha.height)
print(student.count)
print(masha.breathing())