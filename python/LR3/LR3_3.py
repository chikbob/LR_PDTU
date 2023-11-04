print("Введіть число", end=": ")
num = int(input())
print("Введіть ступінь", end=": ")
degree = int(input())


def calc(num, deg):
    final = num**deg
    print(f"{num}^{deg} = {final}")


calc(num, degree)
