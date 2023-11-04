from random import randint

for i in range(5):
    print("Введіть Ім'я:", end=" ")
    name = input()
    print("Введіть По батькові:", end=" ")
    surname = input()
    print("Введіть назву івенту:", end=" ")
    event = input()
    date = randint(1, 5)
    print("Введіть місяць події:", end=" ")
    month = input()

    fullName = [name, surname]
    fullMass = [fullName, event, month]

    print(
        f"Шановний(а), {fullMass[0][0]} {fullMass[0][1]}!\nЗапрошуємо Вас на {fullMass[1]}.\nДата події: {date} {fullMass[2]}.\nЗ повагою, Василю.\n"
    )
