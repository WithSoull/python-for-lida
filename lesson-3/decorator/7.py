def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Вызов функции '{func.__name__}', количество вызовов: {wrapper.call_count}")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@count_calls
def greet():
    print("Привет!")

greet()
greet()

