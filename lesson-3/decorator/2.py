import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Вызов декорированной функции")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def add(a, b):
    """Сложение двух чисел."""
    return a + b

print(add(3, 5))
print(add.__name__)  # Будет "add" вместо "wrapper"

