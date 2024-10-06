from turtle import Turtle
import random

tur = Turtle()
colors = ["AliceBlue", "azure", "beige", "bisque", "blue", "brown", "CadetBlue", "chartreuse", "chocolate", "DarkBlue", "DarkGrey", "DarkOrange", "DarkRed", "DarkSeaGreen", "DarkViolet", "gold", "GreenYellow", "HotPink", "IndianRed", "LawnGreen", "magenta", "orange", "pink", "yellow"]
for i in range(3,9):
    angle = 360/i
    tur.pencolor(random.choice(colors))
    for _ in range(i):
        tur.forward(100)
        tur.right(angle)

tur.screen.mainloop()