from random import randint
import numpy as np

n = 5

matrix = np.random.rand(n, n).round(4) * 100
# Виведення матриці на екран
print("Матриця:")
for row in matrix:
    print(row)

# Знаходження мінімального елемента нижче побічної діагоналі
min_element = float('inf')
for i in range(n):
    for j in range(n):
        if i + j > n - 1:
            if matrix[i][j] < min_element:
                min_element = matrix[i][j]

# Знаходження твору ненульових елементів останнього рядка
product = 1
for element in matrix[n - 1]:
    if element != 0:
        product *= element

# Виведення результатів
print("Мінімальний елемент нижче побічної діагоналі:", min_element)
print("Твір ненульових елементів останнього рядка:", round(product, 2))
