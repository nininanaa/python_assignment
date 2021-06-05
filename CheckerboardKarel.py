from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
Name: 
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""



def main():
    """
    pre-condition:
    Karel is at ave 1 str 1.
    post-condition:
    1,1 3,1 5,1 ... etc has beepers
    2,2 4,2 6,2 ... etc has beepers

    """
    put_beeper()
    while True:
        for i in range(2):
            custom_move()
        put_beeper()


def custom_move():
    if front_is_clear():
        move()
    else:
        if facing_east():
            turn_left()
            move()
            turn_left()
        else:
            turn_right()
            move()
            turn_right()


def turn_right():
    for i in range(3):
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)