from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_back():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear():
    tim.clear()
    tim.teleport(0,0)

screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_back, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
screen.onkeypress(clear, "c")

screen.exitonclick()