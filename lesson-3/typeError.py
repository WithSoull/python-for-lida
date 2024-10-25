try:
    result = "10" + 5
except TypeError as e:
    print(f"Ошибка: {e}")
finally:
    print("Я выполнюсь в любом случае")
