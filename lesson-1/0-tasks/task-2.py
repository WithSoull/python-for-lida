numbers = [1, 5, 3, 6, 2, 8]
result = 0

for num in numbers:
    if num > 4:
        result += num
    else:
        result -= num

print(result)
