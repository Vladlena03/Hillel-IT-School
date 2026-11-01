import keyword
import string

name = input ("Введите имя переменной: ")

result = True
if not name:
    result = False
elif name[0].isdigit():
    result = False
elif any(letter.isupper() for letter in name):
    result = False
elif " " in name:
    result = False
elif "__" in name:
    result = False
elif any(symbol in string.punctuation.replace ("_", " ") for symbol in name):
    result = False
elif keyword.iskeyword(name):
    result = False
elif not all(symbol.isascii() and (symbol.islower() or symbol.isdigit() or symbol == "_") for symbol in name):
    result = False

print(result)