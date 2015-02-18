from math import sqrt
from random import randint
from sys import argv
from turtle import backward, colormode, exitonclick, forward, hideturtle, left, pencolor, right, speed


def tree(depth, size):
	pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
	if depth <= 0:
		return
	size /= sqrt(2)
	forward(size)
	left(90)
	tree(depth-1, size)
	right(180)
	tree(depth-1, size)
	left(90)
	backward(size)


def main(argv):
	depth = int(argv[1])
	size = int(argv[2])
	colormode(255)
	pencolor(0, 0, 0)
	speed(0)
	hideturtle()
	right(90)
	forward(size/2)
	left(180)
	tree(depth, size)
	exitonclick()


if __name__ == "__main__":
	if len(argv) == 1:
		argv += ["12", "400"]
	main(argv)
