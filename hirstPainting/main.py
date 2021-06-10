import turtle as t
import random
reginald = t.Turtle()
screen = t.Screen()
t.colormode(255)
color_list = [(239, 242, 248), (216, 148, 92), (221, 78, 57), (45, 94, 146), (151, 64, 91), (232, 219, 93), (217, 65, 85), (22, 27, 41), (40, 22, 29), (120, 167, 197), (40, 19, 14), (194, 139, 159), (159, 72, 56), (35, 132, 91), (123, 181, 142), (69, 167, 94), (236, 222, 6), (170, 176, 42), (231, 168, 182), (14, 30, 21), (51, 54, 105), (106, 42, 61), (25, 168, 202), (236, 171, 161), (107, 44, 37), (163, 210, 185), (150, 207, 222)]
reginald.hideturtle()
reginald.penup()
reginald.setheading(225)
reginald.forward(320)
reginald.setheading(0)


def draw_dots():
    for _ in range(9):
        reginald.speed(9)
        reginald.dot(20, random.choice(color_list))
        reginald.fd(50)
        reginald.dot(20, random.choice(color_list))




def turn_left():
    reginald.setheading(90)
    reginald.fd(50)
    reginald.setheading(180)


def turn_right():
    reginald.setheading(90)
    reginald.fd(50)
    reginald.setheading(0)


def make_art():
    for _ in range(5):
        draw_dots()
        turn_left()
        draw_dots()
        turn_right()


make_art()

screen.exitonclick()




