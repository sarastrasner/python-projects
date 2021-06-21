import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("50_states.csv")
list_of_states = states_data.state
states_to_learn = []


# TODO: Write Correct Guesses onto the map
def write_state_onto_map(state_to_map):
    x_cor = int(states_data[states_data.state == state_to_map].x)
    y_cor = int(states_data[states_data.state == state_to_map].y)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x_cor, y_cor)
    t.write(state_to_map, align="center")


# TODO: Keep track of the score with len()
correct_answers = []

# TODO: get user to enter a new answer
while len(correct_answers) < 50:
    # TODO: Convert the guess to Title Case
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Correct", prompt="What's another state's name?").title()
    # TODO: Check if the guess is among the 50 states
    if answer_state == "Exit":
        states_to_learn = [state for state in list_of_states if state not in correct_answers]
        df = pd.DataFrame({'States to Learn': states_to_learn})
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in list_of_states.values:
        # TODO: Record the correct guesses in a list
        correct_answers.append(answer_state)
        write_state_onto_map(answer_state)

