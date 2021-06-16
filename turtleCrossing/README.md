# Turtle Crossing
Similar to that of Frogger, the goal of Turtle Crossing is to cross a busy road and get to the other side without being
hit by a car. This game is built using Object-Oriented Programming, classes, and game logic.

![Turtle Crossing Game](https://media.giphy.com/media/tUyiMvAqwDV2dnlVoz/giphy.gif)

## Basic Game Functionality
1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.
1. Cars are randomly generated along the y-axis and will move in a straight line from the right edge of the screen to the left edge.
1. When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. On the next level, the car speed increases.
1. When the turtle collides with a car, it's game over and everything stops.

## Feature Tasks
1. Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north. If you get stuck, check the video walkthrough in Step 3.
1. Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs. If you get stuck, check the video walkthrough in Step 4.
1. Detect when the turtle player collides with a car and stop the game if this happens. If you get stuck, check the video walkthrough in Step 5.
1. Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle to the starting position and increase the speed of the cars. Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed. If you get stuck, check the video walkthrough in Step 6.
1. Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre. If you get stuck, check the video walkthrough in Step 7.


## [Play this game on Repl.it](https://replit.com/@SaraStrasner/python-projects#turtleCrossing/main.py)

## Run this game locally
```
git clone https://github.com/sarastrasner/python-projects.git
cd python-projects/turtleCrossing
python3 main.py


