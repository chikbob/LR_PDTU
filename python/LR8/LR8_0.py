t = [[-8, -14, -19, -18],
     [25, 28, 26, 20],
     [11, 18, 20, 25],
     ]


def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end=" ")
        print()


def printOnly2DayMatrix(matrix):
    print("№2 Роздрукувати показання термометрів всіх метеостанцій за 2-й день")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == 1:
                print((matrix[i][j]), end=" ")


def average3Station(matrix):
    print("№3 Визначити середню температуру на 3-й метеостанції")
    sum = int()
    for i in range(len(matrix[2])):
        sum += matrix[2][i]
    average = sum / len(matrix[2])
    return average


def searchValue(matrix):
    for i in range(len(matrix)):
        for j in matrix[i]:
            if 24 <= j <= 26:
                index = j
                print(f"День: {matrix[i].index(index) + 1}\t Метеостанція: {i+1} \tГрадус: {j}")


print("Таблиця температури повітря за 4 дні з трьох метеостанцій")
printMatrix(t)
print("<------------------------------------------------------------------>")
print(f"№1 Роздрукувати температуру на 2-й метеостанції за 4-й день і на 3-й метеостанції за 1-й день\n2-а "
      f"метеостанція за 4-й день {t[1][3]}\n3-a метеостанція за 1-й день {t[2][0]}")
print("<------------------------------------------------------------------>")
printOnly2DayMatrix(t)
print("\n<------------------------------------------------------------------>")
print(average3Station(t))
print("<------------------------------------------------------------------>")
print("№4 Роздрукувати, в які дні і на яких метеостанціях температура була в діапазоні 24-26 градусів тепла")
searchValue(t)
