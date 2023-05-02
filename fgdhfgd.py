def a(func):
    def wrapper(x):
        print(x + 10)
    return wrapper
@a
def b(x):
    pass
b(10)