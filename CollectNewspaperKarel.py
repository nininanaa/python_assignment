from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
Name: 
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

"""
    pre-condition:
    Karel is at avenue 3 street 4, facing east. Beeper is at avenue 6, street 3.
    post-condition:
    Karel is at avenue 3 street 4, facing east. Beeper is also at avenue 3 street 5.
"""


def main():
    """
    pre-condition:
    Karel is at avenue 3 street 4, facing east. Beeper is at avenue 6, street 3.
    post-condition:
    Karel is at avenue 3 street 4, facing east. Beeper is also at avenue 3 street 5.
    """
    Ktofrontdoor()
    Kbackhome()


def Ktofrontdoor():
    """
    Karel is at avenue 3 street 4, facing east. Beeper is at avenue 6, street 3.
    Karel goes to the front door, where Beeper is at.
    """

    turn_right()
    move()
    turn_left()
    for i in range(3):
        move()


def Kbackhome():
    """
    Karel picks up the newspaper.
    Karel goes back to avenue 3 street 4 with her newspaper.
    Karel puts down her newspaper.
    """
    pick_beeper()
    turn_around()
    for i in range(3):
        move()
    turn_right()
    move()
    turn_right()
    put_beeper()


def turn_right():
    """
    3 times of turning left equal to turning right once.
    """
    for i in range(3):
        turn_left()


def turn_around():
    """
    2 times of turning left equal to turning around once.
    """
    for i in range(2):
        turn_left()





# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
