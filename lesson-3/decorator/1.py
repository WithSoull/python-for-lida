def greet_decorator(func):
    def wrapper(name):
        print("Начинаем...")
        func(name)
        print("Закончили!")
    return wrapper

@greet_decorator
def greet(name):
    print(f"Привет, {name}!")

greet("Алиса")

