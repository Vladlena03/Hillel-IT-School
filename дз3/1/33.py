a = [1, 2, 3, 4, 5]
b = (len(a)+1) // 2
result = [a[:b], a[b:]]
print(result)