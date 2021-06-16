from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# TODO 1. Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move
#  to the left edge of the screen. No cars should be generated in the top and bottom 50px of the screen
class CarManager:
    def __init__(self):
        self.all_cars = []
        self.make_a_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def make_a_car(self):
        #  TODO: generate a new car only every 6th time the game loop runs.
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            random_x_axis = random.randint(-250, 250)
            new_car.goto(290, random_x_axis)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

