from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.penup()
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    def make_car(self):
        random_chance = random.randint(1, 4)
        if random_chance == 1:
            new_cars = Turtle("square")
            new_cars.penup()
            new_cars.shapesize(stretch_wid=1, stretch_len=2)
            new_cars.color(random.choice(COLORS))
            random_y_position = random.randint(-250, 250)
            new_cars.goto(300, random_y_position)
            self.all_cars.append(new_cars)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT



