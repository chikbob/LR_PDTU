from random import randint

list = []

for i in range(5):
    a = randint(0, 100)
    list.append(a)

print(f"Початковий масив: {list}")


def minAndMax(list):
    list.sort()
    newList = list
    return [newList[0], newList[-1]]


def averageNum(list, change):
    newList = sum(list)
    if change == 0:
        return newList
    else:
        return newList / 5


print(f"Мінімальний і максимальний елемент: {minAndMax(list)}")
print(f"Cума елементів масиву: {averageNum(list, 0)}")
print(f"Середнє арифметичне елементів масиву: {averageNum(list, 1)}")
