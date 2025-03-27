from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, -70 + (30 * turtle_index))
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You've won! The {wining_color} turtle is the winner!")
            else:
                print(f"You've LOST! The {wining_color} turtle is the winner!")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()