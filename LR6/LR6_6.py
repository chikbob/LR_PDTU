from random import randint

inputMassive, indexMassive = [], []


def genList():
    for i in range(randint(5, 30)):
        item = randint(0, 100)
        inputMassive.append(int(item))
    return inputMassive


print(genList())

min = int(input("Введіть мінімальне значення діапазону: "))
max = int(input("Введіть максимальне значення діапазону: "))

print(f"Min = {min}")
print(f"Max = {max}")

for i in inputMassive:
    if min <= i <= max:
        index = inputMassive.index(i)
        indexMassive.append(index)

print(f"Кількість: {len(indexMassive)}")
print(indexMassive)
