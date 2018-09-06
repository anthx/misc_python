#!/usr/bin/env python3
from random import randint

global turnCount
global chosen

def evaluate_guess(x):
    global turnCount
    global chosen
    turnCount = turnCount + 1
    if x > chosen:
        print("lower")
    if x < chosen:
        print("higher")

def verbage(x):
    if x > 1:
        return "turns"
    else:
        return "turn"

def game():
    global turnCount
    global chosen
    turnCount = 0
    
    #choose the bounnds
    a = int(input("Chose a lower bound "))
    b = int(input("Chose an upper bound "))

    #let the game choose the number and show it
    chosen = randint(a,b)

    guess = int(input("Guess the number... "))
    evaluate_guess(guess)

    #while the guess is incorrect, keep guessing
    while guess != chosen:
        guess =  int(input("Guess Again! ? "))
        evaluate_guess(guess)

    #they must have got it right
    if guess == chosen: print("You found it! It took you " + str(turnCount) + " " + verbage(turnCount) + ".")

    if input("Play again? (y or n)") == "y":
        game()

game()
        
