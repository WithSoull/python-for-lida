def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции '{func.__name__}' с аргументами {args} и {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def multiply(a, b):
    return a * b

@log_decorator
def sum3(a, b, c):
    return a + b + c


print(multiply(4, 5))
print(sum3(2, 3, c=4))
