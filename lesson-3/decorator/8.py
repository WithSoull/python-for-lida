def add_prefix(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"Результат: {result}"
    return wrapper

@add_prefix
def get_data():
    return "Данные загружены"

print(get_data())
