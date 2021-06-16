import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
screen.listen()

# TODO 1. Create a turtle player that starts at the bottom of the screen and listens for the "Up" keypress to move
#  the turtle north.
player = Player()
screen.onkey(player.move, "Up")
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.make_a_car()
    car_manager.move_cars()

    # TODO detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # TODO detect a successful crossing
    if player.is_at_finish_line():
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
