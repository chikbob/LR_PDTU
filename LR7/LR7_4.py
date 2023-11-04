from random import randint


def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


inputMassive = []

for i in range(randint(5, 15)):
    inputMassive.append(randint(0, 99))

print("Початковий масив:", inputMassive)

bubbleSort(inputMassive)

print("Відсортований масив:", inputMassive)
