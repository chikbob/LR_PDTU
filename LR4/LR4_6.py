from random import randint

print(f"Розмір масиву:", end=" ")
n = int(input())
massive = []
paired = 0
unpaired = 0

for i in range(n):
    a = randint(20, 100)
    massive.append(a)

print(f"Масив: {massive}")

for i in massive:
    if i % 2 == 0:
        paired += 1
    else:
        unpaired += 1

print(
    f"Кількість парних чисел у масиві: {paired}\nКількість непарних чисел у масиві: {unpaired}"
)
