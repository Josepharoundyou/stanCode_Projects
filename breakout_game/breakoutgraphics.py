"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.p_offset = paddle_offset
        self.p_height = paddle_height
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=(window_height-paddle_offset-paddle_height))

        # Center a filled ball in the graphical window
        self.window_width = window_width
        self.window_height = window_height
        self.ball_radius = ball_radius
        self.ball = GOval(ball_radius * 2, ball_radius * 2, x=(self.window_width / 2 - self.ball_radius),
                          y=(self.window_height / 2 - self.ball_radius))
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.set_ball_speed()

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.set_ball_speed)

        # Draw bricks
        self.brick_cols = brick_cols
        self.brick_rows = brick_rows
        self.brick_width = brick_width
        self.brick_height = brick_height
        for i in range(self.brick_cols):
            for j in range(self.brick_rows):
                bricks = GRect(self.brick_width, self.brick_height)
                bricks.filled = True
                if j <= 1:
                    bricks.fill_color = 'red'
                    bricks.color = 'red'
                elif 1 < j <= 3:
                    bricks.fill_color = 'yellow'
                    bricks.color = 'yellow'
                elif 3 < j <= 5:
                    bricks.fill_color = 'green'
                    bricks.color = 'green'
                elif 5 < j <= 7:
                    bricks.fill_color = 'blue'
                    bricks.color = 'blue'
                self.window.add(bricks, x=i*(brick_width+brick_spacing), y=brick_offset+j*(brick_height+brick_spacing))

    def paddle_move(self, mouse):
        self.paddle.x = mouse.x - self.paddle.width / 2
        self.paddle.y = self.window.height - self.p_offset - self.p_height - self.paddle.height / 2
        if self.paddle.x < 0:
            self.paddle.x = 0
        elif self.paddle.x > self.window.width - self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width

    def set_ball_speed(self):
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx *= -1

    def get_ball_x_speed(self):
        return self.__dx

    def get_ball_y_speed(self):
        return self.__dy

    def set_ball_position(self):
        self.window.add(self.ball, x=(self.window_width / 2 - self.ball_radius),
                        y=(self.window_height / 2 - self.ball_radius))












