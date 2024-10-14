# Создаем кортеж с тремя элементами
person = ("John", 25, "Engineer")

# Распакуем кортеж в три переменные
name, age, profession = person

persons = [person, person, person]

for name, age, profession in persons:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

