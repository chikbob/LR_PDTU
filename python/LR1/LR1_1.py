print(
    "Введіть який приклад хочете розрахувати:\n 1) 20a^3 * (5a)^2 \n 2) -0,4x^5 * (2x^3)^4 \n 3) (-c^3)^2 * 12c^6 \n 4) (3x^6 * y^3)^4 * (-1/81 * x * y^2) \n 5) (-2/3 * ab^5)^3 * 18a^5 * b",
    end="",
)
choice = input()
print("Ваше значення -", choice)

if choice == "1":
    print("Напишіть a: ", end="")
    a = input()
    exception1 = 20 * float(a) ** 3 * (5 * float(a)) ** 2
    print("Результат =", round(exception1, 2))
elif choice == "2":
    print("Напишіть x: ", end="")
    x = input()
    exception2 = -0.4 * float(x) ** 5 * (2 * (float(x) ** 3)) ** 4
    print("Результат =", round(exception2, 2))
elif choice == "3":
    print("Напишіть c: ", end="")
    c = input()
    exception3 = (-float(c) ** 3) ** 2 * 12 * float(c) ** 6
    print("Результат =", round(exception3, 2))
elif choice == "4":
    print("Напишіть x: ", end="")
    x = input()
    print("Напишіть y: ", end="")
    y = input()
    exception4 = (3 * float(x) ** 6 * float(y) ** 3) ** 4 * (
        -1 / 81 * int(x) * float(y) ** 2
    )
    print("Результат =", round(exception4, 2))
elif choice == "5":
    print("Напишіть a: ", end="")
    a = input()
    print("Напишіть b: ", end="")
    b = input()
    exception5 = (-2 / 3 * int(a) * float(b) ** 5) ** 3 * 18 * float(a) ** 5 * float(b)
    print("Результат =", round(exception5, 2))
else:
    print("Помилка! Такого прикладу немає!")
