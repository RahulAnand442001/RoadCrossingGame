from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car:
    def __init__(self):
        self.car_list = []

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_color = choice(COLORS)
            new_car.color(random_color)
            random_Y = randint(-250, 250)
            new_car.goto(300, random_Y)
            self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.backward(STARTING_MOVE_DISTANCE)



