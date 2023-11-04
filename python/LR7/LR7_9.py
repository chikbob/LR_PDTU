from random import randint


def bubble_sort(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True


inputMassive = []

for i in range(randint(5, 15)):
    inputMassive.append(randint(0, 99))

print("Початковий масив:", inputMassive)
bubble_sort(inputMassive)
print("Відсортований масив:", inputMassive)
