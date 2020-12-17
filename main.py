import time

from turtle import Screen
from player import Player
from scoreboard import ScoreBoard
from car_manager import Car

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)

# create objects
player = Player()
score = ScoreBoard()
car_manager = Car()

# event listeners
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    # create and move cars
    car_manager.create_car()
    car_manager.move_cars()
    # detect collision with the car
    if player.ycor() >= 280:
        score.update_scorecard()
        player.reset_position()

    for car in car_manager.car_list:
        if player.distance(car) <= 20:
            game_is_on = False
            print("Game Over !")
screen.exitonclick()
