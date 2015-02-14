from random import randint
from sys import argv
from turtle import colormode, exitonclick, forward, hideturtle, left, pencolor, right, speed


def dragon(depth, size, zig=left, zag=right):
	pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
	if depth <= 0:
		forward(size)
		return 
	size /= 1.41421
	zig(45)
	dragon(depth-1, size, right, left)
	zag(90)
	dragon(depth-1, size, left, right)
	zig(45)


def main(argv):
	colormode(255)
	pencolor(0, 0, 0)
	speed(0)
	hideturtle()
	dragon(int(argv[1]), int(argv[2]))
	exitonclick()


if __name__ == "__main__":
	if len(argv) == 1:
		argv += ["16", "1000"]
	main(argv)
