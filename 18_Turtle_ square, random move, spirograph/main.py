from turtle import Turtle, Screen
import random

# Here I'v created 3 separated programs, showing them together to show code
tim = Turtle()
tim.color("brown1")
screen = Screen()
screen.colormode(255)

# MAKING SQUARE AND HEXAGON :)
for i in range(3,11):
    for j in range(i):
        tim.forward(100)
        tim.right(360 / i)
    tim.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

# Making turtle to move at random directions
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b

tim.speed('fastest')
tim.pensize(6)
directions = [0,90,180,270]
for i in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

# MAKING Circle to spirograph
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b

tim.speed('fastest')
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen.exitonclick()