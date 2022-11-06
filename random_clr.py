import turtle
import random

t = turtle.Turtle()
R = random.Random()
turtle.colormode(255)


def colour():
    r = R.randint(0, 255)
    g = R.randint(0, 255)
    b = R.randint(0, 255)
    clr = (r, g, b)
    return clr


for _ in range(75):
    t.pencolor(colour())
    t.speed(15)
    t.right(5)
    t.circle(100)

