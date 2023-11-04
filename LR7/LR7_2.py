from random import randint

inputMassive = []
indexMassive = []

for i in range(randint(3, 15)):
    inputMassive.append(randint(0, 4))

checkX = int(input("Введіть число від 0 до 4: "))

for i in range(len(inputMassive)):
    if inputMassive[i] == checkX:
        indexMassive.append(i)

print(f"Масив чисел: {inputMassive}")
print(f"Індекси числа {checkX}: {indexMassive}")
