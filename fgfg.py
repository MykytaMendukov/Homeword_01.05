def my_decorator_func(func): #3
    def wrapper():
        print('bombom bimbim')
        func()
        print('bimka bomka')
    return wrapper
@my_decorator_func #2
def say_hello(): #1
    print('Hello!')
say_hello()

#2
import time
def delay_decorator(func):
    def wrapper(*args,**krargs):
        time.sleep(0.5)
        return func(*args,**krargs)
    return wrapper

@delay_decorator
def sleepy():
    print('I am sleping..')
sleepy()

#3
def cache_decorator(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper()
@cache_decorator
def fibonacci(n):
    if n in (0,1):
        return n
    return fibonacci(n -1) + fibonacci(n - 2)
print(fibonacci(10))