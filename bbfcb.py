def a(func):
    def wrapper(*args, **kwargs):
        k = func(*args, **kwargs) + 100
        print(k)
    return wrapper
@a
def f(*args):
    r = 1
    for i in args:
        r = r * i
    return r
f(1,2,3,4)