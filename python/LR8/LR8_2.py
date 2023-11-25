from random import randint
import numpy as np

n = randint(3, 10)
m = randint(3, 10)

matrix = np.random.rand(n, m).round(4) * 100

print(matrix, "\n")

max_sum = 0  # початкове значення максимальної суми
max_row = []  # рядок з максимальною сумою

# Проходимо по всіх рядках матриці
for row in matrix:
    row_sum = sum(row)  # обчислюємо суму елементів поточного рядка
    if row_sum > max_sum:
        max_sum = row_sum
        max_row = row

# Виводимо рядок з максимальною сумою на екран
print("Рядок з максимальною сумою:", max_row)
