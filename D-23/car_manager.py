from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.level = 0
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self, flag = False):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            self.car = Turtle('square')
            self.car.color(random.choice(COLORS))
            self.car.shapesize(stretch_wid=1, stretch_len=2)
            self.car.penup()
            random_y = random.randint(-250,250)
            self.car.goto(300, random_y)
            self.all_cars.append(self.car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT