print("Введіть число", end=": ")
input = int(input())


def checkDivider(recived):
    a = int()
    while a != recived:
        a += 1
        if (recived % a) == 0:
            print(a, end=" ")


checkDivider(input)
