from math import sqrt
from random import randint
from sys import argv
from turtle import backward, colormode, down, exitonclick, forward, hideturtle, left, pencolor, right, setpos, speed, up


def side(depth, size):
	pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
	if depth <= 0:
		forward(size)
		return
	size /= 3
	side(depth-1, size)
	right(60)
	side(depth-1, size)
	left(120)
	side(depth-1, size)
	right(60)
	side(depth-1, size)


def snow(depth, size):
	for i in range(3):
		side(depth, size)
		left(120)


def main(argv):
	depth = int(argv[1])
	size = int(argv[2])
	colormode(255)
	pencolor(0, 0, 0)
	speed(0)
	hideturtle()
	up()
	setpos(-size/4.0, -size/4.0)
	down()
	snow(depth, size)
	exitonclick()


if __name__ == "__main__":
	if len(argv) == 1:
		argv += ["5", "800"]
	main(argv)
