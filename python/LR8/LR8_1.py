from random import randint
import numpy as np

n = randint(3, 10)
m = randint(3, 10)

matrix = np.random.rand(n, m).round(4) * 100

print(matrix, "\n")


def find_min_max(matrix):
    min_element = matrix[0][0]  # початкове значення мінімального елемента
    max_element = matrix[0][0]  # початкове значення максимального елемента
    min_index = (0, 0)  # індекси мінімального елемента
    max_index = (0, 0)  # індекси максимального елемента

    # Проходимо по всіх елементах матриці
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Перевіряємо, чи поточний елемент є новим мінімальним або максимальним
            if matrix[i][j] < min_element:
                min_element = matrix[i][j]
                min_index = (i, j)
            if matrix[i][j] > max_element:
                max_element = matrix[i][j]
                max_index = (i, j)

    return min_element, min_index, max_element, max_index


min_element, min_index, max_element, max_index = find_min_max(matrix)

# Виводимо результати
print("Мінімальний елемент:", min_element)
print("Індекси мінімального елемента:", min_index)
print("Максимальний елемент:", max_element)
print("Індекси максимального елемента:", max_index)
