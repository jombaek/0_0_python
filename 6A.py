import time

def time_decorator(decorated_func):
    def timed(args):
        ts = time.time()
        print("Start time:", ts)
        result = decorated_func(args)
        te = time.time()
        print("End time:", te)
        print("Execution time:", te - ts)
        return result
    return timed

def counter_decorator(decorated_func):
    def wrapper(*args):
        wrapper.count += 1
        print("Function calls count:", wrapper.count)
        return decorated_func(*args) 
    wrapper.count = 0
    return wrapper


def method_decorator(decorated_method):
    def wrapper(self, x, y, z):
        return decorated_method(self, 3 * x - 7 * y + 15 * z + 18)
    return wrapper