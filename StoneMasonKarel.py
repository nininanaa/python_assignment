from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
Name: 
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""



def main():
    Karelconstruction()
    Karelgoesdown()
    Kareltonextcolumn()

    """
    pre-condition:
    Karel is at avenue 1, street 1,facing east.
    Karel goes go street up till the top the the arch.
    Karel put beeper when there's no beeper on her way up to the top.
    Karel goes down.
    Karel move 4 avenues
    Karel goes go street up till the top the the arch.
    Karel put beeper when there's no beeper on her way up to the top.
    Karel goes down.
    Karel move 3 ave avenues
    post-condition:
    Karel is at the end of the avenue, street 1,facing east.
    """
    # Karel1stclimb()
    Karelnot1sttimeclimb()
# def Karel1stclimb():
#     """
#     Karel goes up, and puts beeper down when there's no beeper.
#     Karel goes down.
#     Karel goes 4 avenue away.
#     """
#
#
# def Karelnot1sttimeclimb():
#     """
#     Karel check if there's wall on the right hand side
#     if none, Karel goes up again and puts beeper down when there's no beeper
#     Karel goes down, and move 4 avenues away.
#     if yes, Karel goes up again and puts beepers down when there's no beeper.
#     Karel goes down, and ensure facing east.
#     """

def Karelconstruction():
    turn_left()
    while not on_beeper():
        put_beeper()
        while front_is_clear():
            move()
            while not on_beeper():
                put_beeper()
    while front_is_clear():
        move()
        while not on_beeper():
            put_beeper()



def Karelgoesdown():
    turn_around()
    while front_is_clear():
        move()


def turn_around():
    for i in range(2):
        turn_left()


def Kareltonextcolumn():
    turn_left()
    for i in range(4):
        move()


def Karelnot1sttimeclimb():
    while front_is_clear():
        Karelconstruction()
        Karelgoesdown()
        Kareltonextcolumn()
    Karelconstruction()
    Karelgoesdown()
    turn_left()






# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
