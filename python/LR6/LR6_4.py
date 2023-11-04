from random import randint, uniform

allNumbers = []
wholeNumbers = []

for i in range(randint(2, 10)):
    a = uniform(0, 100)
    b = randint(0, 100)
    allNumbers.append(a)
    allNumbers.append(b)

print(f"Початковий масив: {allNumbers}")

for i in allNumbers:
    div2 = i % 2
    div3 = i % 3
    if div2 == 0 or div2 == 1 or div2 == 2 or div3 == 0 or div3 == 1 or div3 == 2:
        wholeNumbers.append(i)

print(f"Масив цілих чисел: {wholeNumbers}")
