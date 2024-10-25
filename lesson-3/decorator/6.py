def cache(func):
    cache_dict = {}

    def wrapper(n):
        if n in cache_dict:
            print(f"Возвращаем из кэша для {n}")
            return cache_dict[n]
        else:
            result = func(n)
            cache_dict[n] = result
            return result
    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

