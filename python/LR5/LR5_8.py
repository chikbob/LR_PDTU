print("Введіть слово:", end=" ")
massive = input()

length = len(massive)

flag = 1
i = 0

for i in range(length):
    if massive[i] == massive[length - (i + 1)]:
        k = 1
    else:
        k = 0
        break
    i += 1

flag = flag * k

if flag == 1:
    print(f"{massive} = слово поліндром")

