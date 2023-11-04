print("Введіть натуральне число", end=": ")
point = int(input())
print("Введіть скільки чисел потрібно вивести", end=": ")
n = int(input())


def fibanachi(start, n):
    end = int()
    for n in range(0, n):
        final = end + start
        start = end
        end = final
        print(end, end=" ")


fibanachi(point, n)
