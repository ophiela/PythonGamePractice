from math import *
import random

words = ["cat", "hat", "pop", "sea", "row", "cup", "lake"]
a = random.randrange(0,6)
wordChoice = words[a]
length = len(wordChoice)
count = len(wordChoice)+ 5
user1 = input(("Let\'s play a game of Hangman. The word has {} letters in it. \n You get {} guesses. Guess a letter ").format(length, count))
count = count - 1
char = list(wordChoice)
word = ''
guess = user1
charSorted = sorted(char)
while count > 0:
    if guess in char:
        print("Great Guess!")
        word = word + guess
        count = count -1
        charGuess = list(word)
        charGuessSort = sorted(charGuess)
        if charGuessSort == charSorted:
            print("You got it!")
            break
        else:
            guess = input("Please guess again. ")
    else:
        guess = input("Sorry, try again. ")
        count = count -1
print(("The word was {}. Thanks for playing!").format(wordChoice))

