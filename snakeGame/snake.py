from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# TODO create a Snake class
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # TODO crete a create_snake method
    def create_snake(self):
        x_coordinate = 0
        for _ in range(3):
            t = Turtle("square")
            t.color("white")
            t.penup()
            t.setposition(x_coordinate, 0)
            x_coordinate -= 20
            self.segments.append(t)

    # TODO create a snake.move() method
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # TODO create methods for UP (90 degrees), RIGHT (0 degrees), DOWN (270 degrees), LEFT (180 degrees)
    # TODO hint: use setheading
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
