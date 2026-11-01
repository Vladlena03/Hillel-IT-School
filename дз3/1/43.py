import random

num = [random.randint(1, 10) for i in range(random.randint (3, 10))]
res = [num[0], num[2], num[-2]]
print(num)
print(res)

