import random


""" Create an variable for words or
create a variable of words for each level?"""

"""Easy mode only 4-6 characters Normal Mode 6-8
characters Hard Mode 8+ characters"""

"""At the start of the game tell users
how many letters thats in the word"""

"""The user gets one letter guess per round if they
enter more than one tell user the input is invalid and try again"""


print("Welcome to the word guess of doom!!")


word_file = open("words.txt").read().splitlines()
random_word = random.choice(word_file)

# display = ('_')


# def easy(random_word):

#     for char in random_word:
#         if len(random_word) >= 4 and len(random_word) <= 6:
#             easy_tier = []
#             easy_tier.append(random_word)
#         return easy_tier


# def medium(random_word)
# def DOOM!!(random_word)


# answer = input("\n Enter Yes or No")


# if answer == "Yes":
#     print("Excellent")
# elif answer == "No":
#     print("exit")

# print("Length of the word:", len(random_word))
# guess = input("Guess the word: ")

letter_guess = []
guesses = 8


# while not exit:
#     for char in random_word:
#         if char.lower() in letter_guess:
#             print(char, end=" ")
#         else:
#             print("_", end=" ")
#     print("")
#     exit = True

#     guess = input(f"Letters guessed left {guesses}, Try again: ")
#     letter_guess.append(guess.lower())
#     if guess.lower() not in random_word.lower():
#         guesses -= 1
#         if guesses == 0:     
#             exit = True


# if exit:
#     print(f"Congratulations you win! The word was {random_word}")
# else:
#     print(f"Hahahahahaha you lose! The word was {random_word}")

while guesses > 0:
    wrong_guesses = 0
    for char in random_word:
        if char in letter_guess:
            print(char, end=" ")
        else:
            print("_", end=" ")
            wrong_guesses += 1
    if wrong_guesses == 0:
        print("\n Congrats!! You win!")
        print("\n The word is:  ", random_word)
        break

    guess = input("\n Make your guess:")
    letter_guess += guess

    if guess not in random_word:
        guesses -= 1
        print("Haha wrong choice")
        print("You have", + guesses, 'more guesess')

        if guesses == 0:
            print("Hahahahaha you lose!!")
            print("The word is: ", random_word)
