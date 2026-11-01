import numbers

a = [0, 1, 34, 7, 0]
b = a.count(0)

for i in range(b):
    a.remove(0)
    a.append(0)

print(a)