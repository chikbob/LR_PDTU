from random import randint


def getElementOrder(arr):
    indices = list(range(len(arr)))

    indices.sort(key=lambda x: arr[x])

    return indices


inputMassive = []

for i in range(randint(5, 15)):
    inputMassive.append(randint(0, 99))

print("Початковий масив:", inputMassive)

# Отримуємо номери елементів у порядку зростання
elementOrder = getElementOrder(inputMassive)

print("Номери елементів у порядку зростання:", elementOrder)
