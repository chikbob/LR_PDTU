import math

print("Введіть натуральне число", end=": ")
num = int(input())


def calc():
    global num
    newNum = math.factorial(int(num))
    return newNum


print(calc())
