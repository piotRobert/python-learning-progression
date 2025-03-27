import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract('image.jpg',30)
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
screen = Screen()
screen.colormode(255)
color_list = [(46, 92, 144), (170, 13, 26), (34, 44, 62), (141, 80, 44), (228, 154, 7), (161, 57, 88), (211, 162, 101), (37, 144, 46), (68, 34, 47), (235, 219, 63), (225, 223, 4), (48, 45, 93), (22, 51, 47), (50, 40, 36), (88, 195, 171), (117, 162, 171), (247, 90, 16), (18, 96, 49), (211, 56, 76), (155, 23, 19), (187, 143, 156), (60, 167, 91), (46, 149, 196), (226, 177, 167), (163, 209, 182), (227, 171, 180)]

turtle = Turtle()
turtle.speed('fastest')
turtle.penup()
turtle.setheading(225)
turtle.fd(300)
turtle.setheading(0)

for i in range(1,11):
    for _ in range(10):
        turtle.dot(20, random.choice(color_list))
        turtle.fd(50)
    turtle.setheading(90)
    turtle.fd(50)
    turtle.setheading(180)
    turtle.fd(500)
    turtle.setheading(0)

screen.exitonclick()