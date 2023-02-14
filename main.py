import random
from colorama import Fore, Back, Style

words = [ "viens", "divi", "tris", "cits" ]

while True:
    word = random.choice(words)
    guessedWord = list("_" for _ in word)
    lives = 5
    print(word)

    while lives > 0 and "".join(guessedWord) != word:
        inp = input(f"Vārds ({len(word)} burti): ")
        if len(inp) != len(word):
            continue

        guessedWord = list("_" for _ in word)
        for i in range(0, len(word)):
            if inp[i] == word[i]:
                print(f"{Back.GREEN}{inp[i]}{Style.RESET_ALL}", end="")
                guessedWord[i] = inp[i]
            elif inp[i] in word:
                print(f"{Back.YELLOW}{inp[i]}{Style.RESET_ALL}", end="")
            else:
                print(f"{inp[i]}", end="")
        print()

        lives -= 1

        print(f"Dzīvības: {lives}")
        print(guessedWord)

    if lives > 0:
        print("Uzvarējām")
    else:
        print("Zaudējām")

    if input("Vai sākt jaunu spēli? y/n").lower() != "y":
        break