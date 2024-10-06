from turtle import Turtle, Screen
screen = Screen()
tur = Turtle()

def right():
    tur.setheading(0)
    # tur.forward(20)
def up():
    tur.setheading(90)
    # tur.forward(20)
def left():
    tur.setheading(180)
    # tur.forward(20)
def down():
    tur.setheading(270)
    # tur.forward(20)
def space():
    tur.forward(20)
def clear_screen():
    tur.clear()
    tur.penup()
    tur.home()
    tur.pendown()

screen.listen()
screen.onkey(fun=right, key="Right")
screen.onkey(fun=up, key="Up")
screen.onkey(fun=left, key="Left")
screen.onkey(fun=down, key="Down")
screen.onkey(fun=space, key="space")
screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()