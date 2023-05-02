def cache(func):
    d = {}
    def wrapper(*args):
        r = func(*args)
        d[args] = r
        return r, d
    return wrapper
@cache
def func(a, b):
    return a * b
print(func(8,4))