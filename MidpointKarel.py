from karel.stanfordkarel import *

"""
File: MidpointKarel.py
Name: 
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    TODO:
    """
    flag_path()
    turn_around()
    while on_beeper():
        move()
        if not on_beeper():
            turn_around()
            move()
            move()
            if on_beeper():
                turn_around()
                move()
                pick_beeper()
                turn_around()
                move()

        elif not front_is_clear():
            pick_beeper()
            turn_around()
            move()
    turn_around()
    move()


    # if not front_is_clear():
    #     pick_beeper()
    #     turn_around()

def front_is_beeper():
    move()
    on_beeper()
    pick_beeper()
    turn_around()

def flag_path():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()

def turn_around():
    for i in range(2):
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
