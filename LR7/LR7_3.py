import random

array = []
array_size = int(input("Задайте розмір масиву: "))

for i in range(array_size):
    array.append(random.randint(1, 100))

min_element = min(array)
first_min_index = array.index(min_element)

max_element = max(array)
last_max_index = len(array) - 1 - array[::-1].index(max_element)

print("Масив:", array)
print("Номер першого мінімального елемента:", first_min_index)
print("Номер останнього максимального елемента:", last_max_index)
