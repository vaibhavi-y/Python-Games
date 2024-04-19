#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Vaibhavi Yadav
#
# Created:     30-03-2024
# Copyright:   (c) Vaibhavi Yadav 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random

def random_word():
    words = ["Apple", "Bat" ,"Zebra", "Python", "C",
             "C++", "Java" ,"Guava" , "Dog", "Engineering",
             "Ruby", "Php" ,"Angular", "Hat" ,"Lion" ]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def main() :
    print("Welcome to Word Guessing Game!")
    name = input("My name is :- ")
    age = int(input("My age is :- "))


    if age<=10:
        print("You are not eligible")
        print("Ooops!!! next time")
        return
    else:
        print("You are eligible")
        print("Have a great experience", name, "!!!")

    word_to_guess = random_word()
    guessed_letters = []
    attempts = 10

    print("The word contains", len(word_to_guess), "letters.")
    print(display_word(word_to_guess, guessed_letters))

    while True:
        guess = input("Guess a letter: ")

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_to_guess:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            attempts -= 1
            print("Incorrect guess. You have", attempts, "attempts left.")
            if attempts == 0:
                print("Game over! The word was:", word_to_guess)
                break

        displayed = display_word(word_to_guess, guessed_letters)
        print(displayed)

        if "_" not in displayed:
            print("Congratulations! You guessed the word:", word_to_guess)
            break

if __name__ == "__main__":
    main()



