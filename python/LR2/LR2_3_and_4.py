from random import randint

sum = 0
x = 0
average = float()

print("Вводити числа з клавіатури або брати випабкові числа? 0 - з клавіатури, 1 - випадкові")
print("Ваш варіант", end=": ")
change = int(input())

if change == 0:
    print("Скільки чисел ви хочете ввести? ", end="")
    n = int(input())

    for x in range (x, n):
        print("Введіть", x+1 ,"число", end=": ")
        num = int(input())
        sum += num
        average = sum/n
        x += 1
    print("Середнє арифметичне сумми чисел введених користувачем =", average)

elif change == 1:
    print("Скільки чисел ви хочете ввести? ", end="")
    n = int(input())

    for x in range (x, n):
        num = int(randint(1,100))
        print("Число під номером:", x+1 ,"=", num)
        sum += num
        average = sum/n
        x += 1
    print("Середнє арифметичне сумми чисел введених користувачем =", format(average, '.2f'))
    
else: 
    print("Помилка! Такого варіанту вибору не існує!")