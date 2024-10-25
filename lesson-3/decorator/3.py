def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции '{func.__name__}' с аргументами {args} и {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def multiply(a, b):
    return a * b

print(multiply(4, 5))

