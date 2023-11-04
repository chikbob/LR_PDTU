def inputWord():
    print("Введіть слово (не меньше 8 букв):", end=" ")
    global word
    word = input()
    return word


inputWord()

while len(word) < 8:
    print("Введено слово замале! Введіть слово більшого розміру!")
    del word
    inputWord()

print(word[0:8])

print("<--------------------->")
if int(len(word)) % 2 == 0:
    size = int((len(word) / 2) - 2)
    print(word[size:-size])
else:
    size = int(len(word) / 3)
    print(word[size: -size + 1])

print("<--------------------->")

print(word[:-6:-1])
