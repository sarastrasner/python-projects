from turtle import Turtle
FONT = ("Courier", 24, "normal")


# TODO Create a scoreboard that keeps track of which level the user is on.
#  Every time the turtle player does a successful crossing, the level should increase.
#  When the turtle hits a car, GAME OVER should be displayed in the centre.
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 265)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=FONT)
