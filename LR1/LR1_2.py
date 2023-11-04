print("Введіть першу змінну: ", end="")
a = int(input())

print("Введіть другу змінну: ", end="")
b = int(input())

print()
print("<------------------------------------>")
print()

print("Сумма (a + b)")
sum = a + b
print(sum)
print()

print("Різниця (a - b)")
min = a - b
print(min)
print()

print("Множення (a * b)")
multy = a * b
print(multy)
print()

print("Ділення (a / b)")
if b == 0:
    print("Помилка! На нуль ділити неможливо!")
else:
    degree = a / b
    print(degree)
print()

print("Цілочисленне ділення (a // b)")
if b == 0:
    print("Помилка! На нуль ділити неможливо!")
else:
    integerDegree = a // b
    print(integerDegree)
print()

print("Зведення у ступінь першої змінної (a^2)")
expo1 = a**2
print(expo1)
print()

print("Зведення у ступінь другої змінної (b^2)")
expo2 = b**2
print(expo2)

print()
print("<------------------------------------>")
print()

print("Переклад у двійкову, вісімкову та шістнадцяткову систему числення")
print()

print("Переклад у двійкову")
print("a")
binary_a = bin(a)
print(binary_a)
print("b")
binary_b = bin(b)
print(binary_b)
print()

print("Переклад у вісімкову")
print("a")
octal_a = oct(a)
print(octal_a)
print("b")
octal_b = oct(b)
print(octal_b)
print()

print("Переклад у шістнадцяткову")
print("a")
hexadecimal_a = hex(a)
print(hexadecimal_a)
print("b")
hexadecimal_b = hex(b)
print(hexadecimal_b)
print()

print("<------------------------------------>")
print()
