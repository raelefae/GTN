# "Guess the number" mini-project
# to be used with http://www.codeskulptor.org/

import simplegui
import random
import math

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randint(0, 100)

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    secret_number = random.randint(0, 100)

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    secret_number = random.randint(0, 1000)
    
def input_guess(guess):
    # main game logic goes here	
    iguess = int(guess)
    print "Guess is", iguess
    #print "Secret number is", secret_number
    if iguess > secret_number:
        print "Lower!"
    elif iguess < secret_number:
        print "Higher!"
    elif iguess == secret_number:
        print "Correct! New secret number generated."
        new_game()

    
# create frame
frame = simplegui.create_frame('Testing', 100, 200)

# register event handlers for control elements and start frame
frame.add_button('0-100', range100, 100)
frame.add_button('0-1000', range1000, 100)
frame.add_button('new game', new_game, 100)
frame.add_input("Guess a number, default is 0-100", input_guess, 200)

frame.start()

# call new_game 
new_game()