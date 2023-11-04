from random import randint

inputMassive = []
dev3Massive = []

for i in range(randint(5, 15)):
    inputMassive.append(randint(0, 100))

print(inputMassive)

flag = 0

for i in range(len(inputMassive)):
    while inputMassive[i] % 3 == 0:
        dev3Massive.append(inputMassive[i])
        flag = 1
        break
    else:
        i += 1

allText = ''

if flag == 1:
    if len(dev3Massive) > 1:
        for i in dev3Massive:
            item = "".join(str(i))
            allText += f"{item} "
        print(f"У масиві є числа кратні 3, це {allText}")
    else:
        for i in dev3Massive:
            print(f"У масиві є число кратне 3, це {i}")
