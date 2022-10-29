"""
File: bouncing_ball
Name:Joseph Huang
-------------------------
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40


window = GWindow(800, 500, title='bouncing_ball.py')
oval = GOval(SIZE, SIZE, x=START_X, y=START_Y)
oval.filled = True
oval.fill_color = 'black'
window.add(oval)
vy = 0
times = 3


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(bounce)


def bounce(mouse):
    """
    this function will make the ball
    to start bouncing at (START_X, START_Y)
    """
    global times, vy
    # The variable 'switch' will decide if the ball will move up or down.
    switch = True
    # Only runs for 3 times.
    if times > 0:
        times -= 1
        # If the ball moves across the right boarder, restart the ball at (START_X, START_Y)
        while oval.x <= window.width:
            if switch:
                oval.move(VX, vy)
                vy += GRAVITY
                if oval.y >= window.height or oval.y+vy >= window.height:
                    vy = -vy*REDUCE
                    # Change direction.
                    switch = False
                pause(DELAY)
            else:
                oval.move(VX, vy)
                # To reduces y velocity to REDUCE of itself.
                vy += GRAVITY
                if vy >= 0:
                    # Change direction.
                    switch = True
                pause(DELAY)
        # To restart the ball at (START_X, START_Y)
        window.add(oval, START_X, START_Y)
        vy = 0


if __name__ == "__main__":
    main()
