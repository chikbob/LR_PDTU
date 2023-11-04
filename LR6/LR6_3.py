word = input("Введіть слово:")

list = list(word)
i = 1

try:
    while list[i - 1] == list[-i]:
        i += 1
        if i == len(list):
            print("Слово поліндром")
    else:
        print("Слово не поліндром")
except:
    i
