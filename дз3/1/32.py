numbers = [12, 4, -1, 87]
print(numbers)

if len(numbers) > 1:
    numbers.insert(0, numbers [-1])
    numbers = numbers[:-1]
    print(numbers)