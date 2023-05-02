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
        time.sleep(3)
        return func(*args,**krargs)
    return wrapper

@delay_decorator
def sleepy():
    print('I am sleping..')
sleepy()