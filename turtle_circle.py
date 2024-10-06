import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
tur = Turtle()
# tur.speed("fastest")
s1 = Screen()

while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tur.pencolor((r, g, b))
    tur.circle(100)
    tur.left(5)
    if tur.heading()==0:
        break
s1.exitonclick()