print("Введіть слово:", end=" ")
word = input()

n = 0
even = []
odd = []

for i in word:
    n += 1
    massive = [i, n]
    even.append(massive)
    odd.append(massive)

even = even[1::2]  # Парні числа у массиві
odd = odd[::2]  # Непарні числа у массиві

print("Парні номера")

for i in even:
    print(f"{i[0]}{i[1]}")

print("Непарні номера")

for i in odd:
    print(f"{i[0]}{i[1]}")
