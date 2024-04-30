import datetime

def time_decorator(func):
    def wrapper():
        start = datetime.datetime.now()
        res = func()
        end = datetime.datetime.now()
        print((end - start).seconds)
        return res
    return wrapper
