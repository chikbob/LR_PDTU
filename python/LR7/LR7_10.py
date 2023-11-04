from random import randint


def sortAndFindMaxRepeating(arr):
    arr.sort()

    maxCount = 0
    maxRepeating = 0
    currentCount = 1

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            currentCount += 1
        else:
            if currentCount > maxCount:
                maxCount = currentCount
                maxRepeating = arr[i - 1]
            currentCount = 1

    if currentCount > maxCount:
        maxCount = currentCount
        maxRepeating = arr[-1]

    return maxRepeating, maxCount


inputMassive = []

for i in range(randint(20, 50)):
    inputMassive.append(randint(1, 15))

print(inputMassive)
result, current_count = sortAndFindMaxRepeating(inputMassive)

print(f"Максимальний повторюваний елемент: {result}, він повторюється {current_count} рази")
