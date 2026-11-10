def popular_words(text, words):
    text = text.lower().split()
    result = {}

    for word in words:
        result[word] = text.count(word)

    return result

print(popular_words("One two one three ONE",["one", "two", "three", "four"]))