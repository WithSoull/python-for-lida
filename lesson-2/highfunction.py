# map и filter
def square(x):
    return x * x

def cube(x):
    return x * x * x

print(list(map(square, [1, 2, 3, 4, 5])))

# ==============================

def is_odd(x):
    return x % 2 == 0

print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

# ==============================

def change_data(f, x, y):
    return f(x, y)

# print(change_data(square, 10))
# print(change_data(cube, 10))

print(change_data(lambda x, y: x * y, 10, 20))

