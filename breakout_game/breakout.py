"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.graphics.gobjects import GLabel
import random

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts
graphics = BreakoutGraphics()
vx = graphics.get_ball_x_speed()
vy = graphics.get_ball_y_speed()
Check = True
times = NUM_LIVES
Count = graphics.brick_cols*graphics.brick_rows


def main():
    """
    To make the ball starts after mouse clicked.
    """
    onmouseclicked(check_mouse)


def check_mouse(mouse):
    """
    To make sure if the ball is moving or waiting to start.
    """
    global Check, times
    if Check:
        Check = False
        times -= 1
        if times >= 0:
            ball_move()
            graphics.set_ball_position()


def ball_move():
    """
    To define how does the ball move.
    """
    global vx, vy, Check
    while graphics.ball.y < graphics.window.height:
        graphics.ball.move(vx, vy)
        check_for_collisions()
        check_for_paddle()
        check_for_walls()
        if Count == 0:
            label = GLabel("You Win !!")
            label.font = '-50'
            graphics.window.add(label, x=graphics.window_width / 2, y=graphics.window_height / 2)
            break
        pause(FRAME_RATE)
    Check = True
    print(vx, vy)


def check_for_walls():
    """
    To check if the ball reaches any side of the walls except for the bottom one.
    """
    global vx, vy
    if graphics.ball.x < 0 or graphics.ball.x > graphics.window.width - graphics.ball.width:
        vx *= -1
    if graphics.ball.y < 0:
        vy *= -1


def check_for_collisions():
    """
    To check if the ball reaches any brick, if it does, then eliminate the one that it reaches.
    """
    global vx, vy, Count
    get_obj1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
    get_obj2 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
    get_obj3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
    get_obj4 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                             graphics.ball.y + graphics.ball.height)
    if get_obj1 is not None and get_obj1 is not graphics.paddle:
        graphics.window.remove(get_obj1)
        Count -= 1
        vy = -vy
    elif get_obj2 is not None and get_obj2 is not graphics.paddle:
        graphics.window.remove(get_obj2)
        Count -= 1
        vy = -vy
    elif get_obj3 is not None and get_obj3 is not graphics.paddle:
        graphics.window.remove(get_obj3)
        Count -= 1
        vy = -vy
    elif get_obj4 is not None and get_obj4 is not graphics.paddle:
        graphics.window.remove(get_obj4)
        Count -= 1
        vy = -vy


def check_for_paddle():
    """
    To check if the ball reaches the paddle.
    """
    global vx, vy
    get_obj5 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
    get_obj6 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                             graphics.ball.y + graphics.ball.height)
    if get_obj5 or get_obj6 is graphics.paddle:
        # bounce
        vy = -graphics.get_ball_y_speed()


if __name__ == '__main__':
    main()
