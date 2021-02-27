import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.make_car()
    cars.move_car()
    for auto in cars.all_cars:
        if auto.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()
    if turtle.at_end():
        turtle.reset_position()
        cars.increase_speed()
        scoreboard.level_up()



screen.exitonclick()