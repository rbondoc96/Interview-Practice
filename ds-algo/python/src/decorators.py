import time

def timer(func):

    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()

        elapsed = end - start

        print(f"{func.__name__} took {elapsed} seconds.")

        return value

    return wrapper