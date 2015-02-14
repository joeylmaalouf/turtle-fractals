from random import randint
from sys import argv
from turtle import backward, colormode, exitonclick, forward, hideturtle, left, pencolor, right, speed


def triangle(depth, size):
	pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
	if depth <= 0:
		return
	size /= 2
	forward(size)
	right(120)
	triangle(depth-1, size)
	forward(size)
	right(120)
	triangle(depth-1, size)
	forward(size)
	right(120)
	triangle(depth-1, size)


def main(argv):
	colormode(255)
	pencolor(0, 0, 0)
	speed(0)
	hideturtle()
	backward(int(argv[2])/4)
	left(60)
	triangle(int(argv[1]), int(argv[2]))
	exitonclick()


if __name__ == "__main__":
	if len(argv) == 1:
		argv += ["6", "480"]
	main(argv)
