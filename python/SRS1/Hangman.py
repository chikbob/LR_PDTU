import random
import time


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["біт", "радість", "кольчуга", "перука", "барометр", "автохром", "градусник", "купа", "лавочник", "светр", "павич", "коляска"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""


def play_loop():
    global play_game
    play_game = input("Ви хочете пограти ще раз? т = так, н = ні \n")
    play_game = play_game.lower()
    if play_game == "т" or play_game == "так" or play_game == "y" or play_game == "yes":
        main()
        hangman()
    else:
        print("Дякую за гру!")


def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("Слово: " + display + " Введіть вашу букву (українською): \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Введені дані не вірні! Спробуйте ще раз!\n")
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Спробуйте іншу букву.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Такої букви немає. " + str(limit - count) + " спроб залишилось\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Такої букви немає. " + str(limit - count) + " спроб залишилось\n")

        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Такої букви немає. " + str(limit - count) + " спроб залишилось\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Такої букви немає. " + str(limit - count) + " спроб залишилось\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Такої букви немає. Спроб не залишилось!!!\n")
            print("Слово було:", already_guessed, word)
            play_loop()

    if word == '_' * length:
        print("Перемога! Ви вгадали слово!")
        play_loop()

    elif count != limit:
        hangman()


main()

hangman()
