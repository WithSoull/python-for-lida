import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции '{func.__name__}': {end_time - start_time:.4f} сек")
        return result
    return wrapper

@timer_decorator
def compute_square_sum(n):
    return sum(i * i for i in range(n))

compute_square_sum(100000)

