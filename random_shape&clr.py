from turtle import Turtle
from turtle import Screen
from random import Random
t = Turtle()
r = Random()

t.shape("turtle")
colours = ["red", "green", "blue", "grey", "violet", "brown", "black", "indigo", "yellow"]
n = 11
for num in range(n):
    if num >= 3:
        t.color(r.choice(colours))
        angle = 360 / num
        for _ in range(num):
            t.right(angle)
            t.forward(100)










screen = Screen()
screen.exitonclick()
