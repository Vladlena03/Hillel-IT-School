import string
letters = string.ascii_letters
text = input("Введите буквы через дефис:")
start, end = text.split("-")

first = letters.index(start)
last = letters.index(end)

result = letters[first:last + 1]
print(result)