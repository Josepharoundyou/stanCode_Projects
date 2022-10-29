"""
File: sierpinski.py
Name: 
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO:
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order:
	:param length:
	:param upper_left_x:
	:param upper_left_y:
	:return:
	"""
	sierpinski_line(order, length, upper_left_x, upper_left_y)


def sierpinski_line(n, l, x1, y1):
	if n == 0:
		pass
	else:
		line1 = GLine(x1, y1, x1+l, y1)
		line2 = GLine(x1+l, y1, x1+0.5*l, y1+0.866*l)
		line3 = GLine(x1+0.5*l, y1+0.866*l, x1, y1)
		window.add(line1)
		window.add(line2)
		window.add(line3)

		# Left
		sierpinski_line(n - 1, 0.5 * l, x1, y1)
		# Right
		sierpinski_line(n - 1, 0.5 * l, x1 + 0.5 * l, y1)
		# Middle
		sierpinski_line(n - 1, 0.5 * l, x1 + 0.25 * l, y1 + 0.433 * l)




if __name__ == '__main__':
	main()