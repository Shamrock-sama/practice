#-*- coding:UTF-8 -*-

'''
This program creates a 'rock, paper and scissor' game
Author: Zhujin
'''

import random


item = ["rock", "paper", "scissor"]
def rps_rule(guess):
    r = []
    item = ["rock", "paper", "scissor"]
    robot = random.choice(item)
    if guess == robot:
        r = "Tie"
    else:
        if guess == "rock" and robot == "paper":
            r = "Sorry, you lose"
        elif guess == "rock" and robot == "scissor":
            r = "Congratulations! You win"
        elif guess == "paper" and robot == "rock":
            r = "Congratulations! You win"
        elif guess == "paper" and robot == "scissor":
            r = "Sorry, you lose"
        elif guess == "scissor" and robot == "rock":
            r = "Sorry, you lose"
        elif guess == "scissor" and robot == "paper":
            r = "Congratulations! You win"
        else:
            print("Error")
    return r

while True:
    guess = input("Give your guess: ")
    if guess not in item:
        print("Please input a valid guess!")
    else:
        result = rps_rule(guess)
        if result == "Tie":
            print("Tied, give a another shot: ")
        else:
            print(result)
            break