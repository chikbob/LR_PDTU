print("Формула для отримання n-го члена прогресії: an = a1 + (n-1) * d")
print("Введіть перший елемент прогресії (a1): ", end="")
a1 = float(input())
print("Введіть різницю прогресії (d): ", end="")
d = float(input())
print("Введіть кількість елементів прогресії (n): ", end="")
n = int(input())

massive = []

for i in range(n):
    x = a1 + (i-1) * d
    massive.append(x)

print(massive)