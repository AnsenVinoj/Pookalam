
import turtle
from turtle import *
import math


speed(0)


def circ(len,clr):
    penup()
    home()
    goto(0, -(len+50))
    pendown()
    color(clr)
    begin_fill()
    circle(len)
    end_fill()

circ(300,"#3d0706")

home()
goto(0, -50)
def tripatt(len,clr):
    color(clr)
    for i in range(36):
        begin_fill()
        forward(len / math.tan(math.pi / 3.6))
        left(130)
        forward(len / math.sin(math.pi / 3.6))
        left(100)
        forward(len / math.sin(math.pi / 3.6))
        left(130)
        forward(len / math.tan(math.pi / 3.6))
        end_fill()
        left(10)
    left(5)

def draw_polygon(sides, length, color, repeat=0, rotate=0, y_offset=0):

    turtle.penup()
    x, y = turtle.position()
    turtle.setpos(x, y + y_offset)
    turtle.fillcolor(color)
    for _ in range(repeat):
        turtle.begin_fill()
        for _ in range(sides):
            turtle.forward(length)
            turtle.right(360/sides)
        turtle.end_fill()
        turtle.right(rotate)

def draw_flower_petals(petals, r, angle, color, y_offset=0):

    turtle.penup()
    x, y = turtle.position()
    turtle.setpos(x, y + y_offset)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(petals):
        for _ in range(2):
            turtle.circle(r, angle)
            turtle.left(180 - angle)
        turtle.left(360 / petals)
    turtle.end_fill()
    turtle.penup()
    turtle.setpos(x, y)  
    turtle.pendown()

def draw_flower_pattern(color, size, repeat, rotate=10, y_offset=0):

    x, y = turtle.position()
    turtle.setpos(x, y + y_offset)
    turtle.penup()
    turtle.fillcolor(color)
    for _ in range(repeat):
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(size)
            turtle.left(90)
        turtle.end_fill()
        turtle.right(rotate)
tripatt(300,"#cf342b")
tripatt(271, "#f5700a")
tripatt(246,"#fcd349")
tripatt(223,"#EDEDE8")
circ(200,"#3d0706")
circ(182,"#fcd349")




draw_flower_petals(10, 155, 70, "#34501C", y_offset=180)
turtle.left(50)
draw_flower_petals(10, 155, 70, "#EDEDE8", y_offset=180)
turtle.left(50)
draw_flower_petals(10, 155, 70, "#C8520A", y_offset=180)
draw_flower_petals(10, 125, 70, "#3d0706", y_offset=180)
turtle.left(50)
circ(100,"#b21c0e")
draw_polygon(5, 50, "#EDEDE8", repeat=20, rotate=20,y_offset=100)
draw_flower_pattern("#3d0706", 40, 9, 40, y_offset=0)
circ(40,"#b21c0e")
circ(30,"#34501C")

circ(25,"#EDEDE8")
circ(8,"#8A0303")
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.Screen().exitonclick()

