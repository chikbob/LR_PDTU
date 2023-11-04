from random import randint

massive = []

for i in range(20):
    a = [randint(-100, 100) for i in range(5)]
    massive.append(a)

print(massive)