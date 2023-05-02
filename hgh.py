#1
def a(*args):
    x = []
    for i in args:
        x.append(i)
        c = ', '.join(x)
    print(c)
a('Kit Kat', 'Snickers', 'Lion', 'Twix', 'Milky Way')
print()

#2
import random
def b(*args):
    l = []
    m = []
    for i in args:
        l.append(i)
    print(f'Список чисел: {l}')
    m.append(min(l))
    m.append(max(l))
    m = tuple(m)
    print(f'Кортеж з min i max: {m}')
b(random.randint(1,50), random.randint(1,50), random.randint(1,50), random.randint(1,50), random.randint(1,50))
print()

#3
import random
def c(*args):
    print(f'Початкові числа: {args}')
    d = {}
    for i in args:
        d[i] = i**2
    print(f'Кінцевий словник: {d}')
c(random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))
print()

#4
def d(*args):
    l = []
    for i in args:
        if i % 2 == 0:
            l.append(i)
    print(l)
d(1,2,3,4,5,6,7,8,9,10)