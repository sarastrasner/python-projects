from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


def make_turtles():
    coordinate = -100
    for color in colors:
        t = Turtle(shape="turtle")
        all_turtles.append(t)
        t.color(color)
        t.penup()
        t.goto(-230, coordinate)
        coordinate += 30


if user_guess:
    is_race_on = True
else:
    is_race_on = False


def move_turtles(should_race_continue):
    while should_race_continue:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                should_race_continue = False
                winner = turtle.pencolor()
                if winner == user_guess:
                    print(f"You've won! The {winner} turtle is the winner!")
                else:
                    print(f"You've lost. The {winner} turtle won.")

            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


make_turtles()
move_turtles(is_race_on)

screen.exitonclick()
