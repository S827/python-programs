from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2 - t1} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):  # it tookk 3.5 secs as it is using generators under the hood
        i*5


@performance
def long_time1():
    for i in list(range(100000000)):  # it took 36 secs
        i*5


long_time()
long_time1()
