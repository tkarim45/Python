import turtle
import math


def draw_circle(t, x, y, r, col):
    t.fillcolor(col)
    t.begin_fill()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(r)
    t.end_fill()


def draw_rectangle(t, x, y, w, h, col):
    t.fillcolor(col)
    t.begin_fill()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.end_fill()

def draw_sun(t, x, y, r, col):
    t.fillcolor(col)
    t.begin_fill()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(r)
    t.end_fill()


def draw_triangle1(t, x, y, w, h, col):
    t.fillcolor(col)
    t.begin_fill()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(w)
    t.left(120)
    t.forward(w)
    t.left(120)
    t.forward(w)
    t.left(120)
    t.end_fill()


def drawTriangle2(t, x, y, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(length)
    t.left(135)
    t.forward(length / math.sqrt(2))
    t.left(90)
    t.forward(length / math.sqrt(2))
    t.left(135)
    t.end_fill()


def draw_square(t, x, y, w, col):
    t.fillcolor(col)
    t.begin_fill()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(w)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.end_fill()


def draw_house1(t, x, y, w, h, col1, col2):
    draw_triangle1(t, x, y, w, h, col1)
    draw_square(t, x, y - h, w, col2)
    draw_rectangle(t, x + w / 2 - w / 10, y - h + 3 / 2, w / 5, h / 2, "black")
    draw_square(t, x + w / 2 / 10, y - h + 180 / 2, w / 5, "white")
    draw_square(t, x + 50 + w / 2 / 10, y - h + 180 / 2, w / 5, "white")
    draw_square(t, x + w / 2 / 10, y - h + 80 / 2, w / 5, "white")
    draw_square(t, x + 100 + w / 2 / 10, y - h + 180 / 2, w / 5, "white")
    draw_square(t, x + 100 + w / 2 / 10, y - h + 80 / 2, w / 5, "white")


def draw_house2(t, x, y, w, h, col1, col2):
    # draw_triangle1(t, x, y, w, h, col1)
    # draw_square(t, x, y - h, w, col2)
    # draw_rectangle(t, x + w / 2 - w / 10, y - h + 3 / 2, w / 5, h / 2, "black")
    # draw_square(t, x + w / 2 / 10, y - h + 180 / 2, w / 5, "white")
    # draw_square(t, x + 100 + w / 2 / 10, y - h + 180 / 2, w / 5, "white")
    drawTriangle2(t, x, y, 300, col1)
    draw_rectangle(t, x, y - h, w + 150, h, "yellow")
    draw_rectangle(t, x + 80 + w / 2 - w / 10, y - h + 3 / 2, w / 5, h / 2, "black")
    draw_square(t, x + 20 + w / 2 / 10, y - h + 150 / 2, w / 3, "white")
    draw_square(t, x + 115 + 100 + w / 2 / 10, y - h + 150 / 2, w / 3, "white")


def draw_tree(t, x, y, w, h, col1, col2):
    t.left(90)
    draw_rectangle(t, x + 160, y - 150, 150 + w, h - 15, col1)
    draw_circle(t, x + 205, y + h - 5 + 150, 65, col2)


t = turtle.Turtle()  # Create a turtle object
t.speed(10)  # Set the speed of the turtle

draw_house1(t, -350, 10, 150, 150, "red", "green")
draw_house2(t, -100, 10, 150, 150, "red", "yellow")
draw_tree(t, 150, 10, 150, 50, "brown", "green")


t.screen.mainloop()
