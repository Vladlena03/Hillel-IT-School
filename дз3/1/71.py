def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old."


name = input("Введите имя: ")
age = int(input("Введите возраст: "))

result = say_hi(name, age)

print(result)