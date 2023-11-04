print("Введіть кількість ітерацій у ряді Фібаначі: ", end="")
n = int(input())
start = 1
end = 1

print(start, end, end=" ")

for x in range(2, n):
    start, end = end, start + end
    print(end, end=" ")