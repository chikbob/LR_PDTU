from math import cos, sqrt

print("Введіть який приклад хочете розрахувати (1 - 6): ", end="")
choice = input()
print("Ваше значення -", choice)

if choice == "1":
    print("Введіть: A = ", end="")
    A = int(input())

    print("Введіть: B = ", end="")
    B = int(input())

    x = int()
    x = (0.51 * float(x) ** 3 + A * B) / (1 + float(cos(x)) ** 2) + (A / (A + B))

    print("Відповідь: x =", x)

elif choice == "2":
    print("Введіть: A = ", end="")
    A = int(input())

    print("Введіть: B = ", end="")
    B = int(input())

    print("Введіть: C = ", end="")
    C = int(input())

    x = int()
    x = (A * B / C) + (abs(A - B) / cos(float(A) ** 3))

    print("Відповідь: x =", x)

elif choice == "3":
    print("Введіть: A = ", end="")
    A = int(input())

    print("Введіть: B = ", end="")
    B = int(input())

    print("Введіть: X = ", end="")
    X = int(input())

    y = int()
    y = 0.87 * ((abs(float(A**2) + sqrt(B * A))) / X - 1 + (1 + B / 1 - A))

    print("Відповідь: y =", y)

elif choice == "4":
    print("Введіть: X = ", end="")
    X = int(input())

    y = int()
    y = sqrt(abs((X + sqrt(X**2))) / 1 - 2 * X)

    print("Відповідь: y =", y)

elif choice == "5":
    print("Введіть: X = ", end="")
    X = int(input())

    y = int()
    y = (1 + X) ** 2 + sqrt(1 + X**2) / cos(X) ** 2

    print("Відповідь: y =", y)

elif choice == "6":
    print("Введіть: A = ", end="")
    A = int(input())

    print("Введіть: B = ", end="")
    B = int(input())

    print("Введіть: C = ", end="")
    C = int(input())

    print("Введіть: X = ", end="")
    X = int(input())

    y = int()
    y = 0.5 * X - (((A * X) - B) * X - B / X - 1)

    print("Відповідь: y =", y)
