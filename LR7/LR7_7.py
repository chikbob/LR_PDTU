from random import randint


def sortAndCountUnique(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    uniqueCount = 1

    for i in range(1, n):
        is_unique = True
        for j in range(0, i):
            if arr[i] == arr[j]:
                is_unique = False
                break
        if is_unique:
            uniqueCount += 1

    return arr, uniqueCount


inputMassive = []

for i in range(randint(5, 15)):
    inputMassive.append(randint(0, 99))

sortedMassive, uniqueCount = sortAndCountUnique(inputMassive)

print("Відсортований масив:", sortedMassive)
print("Кількість різних чисел:", uniqueCount)
