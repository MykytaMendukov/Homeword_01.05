class student:
    print('hi!')
    def __init__(self, height = 150):
        self.height = height
oleg = student()
print(oleg.height)
masha = student(height=200)
print(masha.height)