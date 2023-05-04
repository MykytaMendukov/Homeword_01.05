def log(func):
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        print(f'Function{func.__name__}, carry {args} and {kwargs}, and bimbim {ret}')
        return ret
    return wrapper


@log
def temperature(c):
    return (c * 1.8) + 32
print(temperature(32))
print(temperature(40))
print(temperature(50))