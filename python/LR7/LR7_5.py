from random import randint


def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    done = False
    while not done:
        while left <= right and arr[left] // 10 < pivot // 10:
            left = left + 1
        while arr[right] // 10 >= pivot // 10 and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[low], arr[right] = arr[right], arr[low]
    return right


def quickSort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quickSort(arr, low, pivot_index - 1)
        quickSort(arr, pivot_index + 1, high)


inputMassive = []

for i in range(randint(5, 15)):
    inputMassive.append(randint(0, 99))

print("Початковий масив:", inputMassive)

quickSort(inputMassive, 0, len(inputMassive) - 1)

print("Відсортований масив за першою цифрою:", inputMassive)
