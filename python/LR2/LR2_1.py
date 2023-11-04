import re
neg = 0
pos = 0
while bool(input):
    print(
        "Введіть будь яке цілочислене число, якщо воно буде = 0, то цикл завершется: ",
        end="",
    )
    input = input()
    checker = re.search("[a-zA-Zа-яА-Я]", input)
    if checker != None:
        print("Помилка! Ви ввели не цілочислене число!")
        continue
    elif int(input) < 0:
        neg += int(input)
    elif int(input) > 0:
        pos += int(input)
    else:
        if int(pos) == 0 and int(neg) == 0:
            print("Першим числом було введено 0!")
            break
        elif int(pos) != 0:
            print("Сумма позитивних чисел:", pos)
        elif int(pos) == 0:
            print("Позитивних чисел не було введено")
        if int(neg) == 0:
            print("Негативних чисел не було введено")
        elif int(neg) != 0:
            print("Сумма негативних чисел:", neg)
        break
    del input
    continue