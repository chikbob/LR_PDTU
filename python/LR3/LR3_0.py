print("Введіть перше число", end=": ")
a1 = int(input())
print("Введіть друге число", end=": ")
a2 = int(input())


def calc(first, second):
    sum = first - second
    print(f"1) процедура без параметрів = {sum}")


def calcIn():
    print("Введіть перше число", end=": ")
    a1 = int(input())
    print("Введіть друге число", end=": ")
    a2 = int(input())
    sum = a1 - a2
    print(f"2) процедура із параметрами = {sum}")


calc(a1, a2)
calcIn()
