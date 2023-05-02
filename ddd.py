import time
def time_function(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('time: ', end_time - start_time)
        return result
    return wrapper()


@time_function
def ex_function():
    time.sleep(2)
print(ex_function())