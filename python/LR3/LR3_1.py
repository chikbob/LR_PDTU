print("число", end=": ")
num = int(input())


def calc(a):
    size = len(str(a))
    print("результат", end=": \n")
    for i in range(size):
        final = int(str(a)[-i - 1])
        print(final)


calc(num)
