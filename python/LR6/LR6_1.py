s = input("Введіть рядок: ")
l = list(str(s))

n = 0
num = []
iter = str()

for i in l:
    if i != "+":
        iter += i
    else:
        num.append(int(iter))
        iter = str()
else:
    num.append(int(iter))
    del iter

print(f"Сума чисел: {sum(num)}")
