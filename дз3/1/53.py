import string

text = input("Введите текст: ")

for symbol in string.punctuation:
    text = text.replace(symbol, "")

words = text.split()
hashtag = "#"

for word in words:
    hashtag = hashtag + word

hashtag = hashtag [:140]
print(hashtag)