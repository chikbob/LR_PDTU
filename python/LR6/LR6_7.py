from random import randint

list, indexMassive = [], []


def genList():
    for i in range(randint(5, 20)):
        item = randint(0, 100)
        list.append(int(item))
    return list


print(genList())

min = int(input("Введіть мінімальне значення діапазону: "))
max = int(input("Введіть максимальне значення діапазону: "))

print(f"Min = {min}")
print(f"Max = {max}")

n = 0
list_copy = list.copy()

# При перевірці, якщо елемент підходить, ми видаляємо його з копії масиву

for i in list:
    if min <= i <= max:
        index = list.index(i)
        indexMassive.append(index)
        del list_copy[n]
    else:
        n += 1

print(f"Кількість: {len(indexMassive)}")
print(f"Масив індексів: {indexMassive}")
print(f"Новий масив після видалення цих елементів: {list_copy}")
