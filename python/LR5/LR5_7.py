print("Введіть суму натуральних чисел:", end=" ")
example = input()

example = example.replace("+", " ")

example = example.split()

sumSTR = str()

for i in example:
    sumSTR += i
print(f"Якщо залишити тип стрінг: {sumSTR}")

sum = int()

for i in example:
    sum += int(i)


print(f"Якщо зробити тип інт: {sum}")
