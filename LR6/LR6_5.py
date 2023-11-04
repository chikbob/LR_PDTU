from re import search

amount = int(input("Введіть кількість значень у масиві: "))

massive = []
massive_int = []


def inputWord(i):
    word = input(
        f"Введіть значення під номером {i + 1}: ")  # не змінюємо значення на числове відразу, бо за умовою задачі потрібно щоб введене значення було string
    if len(word) == 0:
        print("Введене значення не підходить:")
        inputWord(i)
    else:
        return word


for i in range(amount):
    massive.append(inputWord(i))

print(f"Масив: {massive}")

for i in massive:
    if search('[a-zA-Zа-яА-Я]', i) is not None:
        print(f"Введене {i} не є числом! Його буде видалено!")
        amount -= 1
    else:
        i = int(i)
        massive_int.append(i)

sum_massive = sum(massive_int)

print(f"Середнє арифметичне: {sum_massive / amount}")
