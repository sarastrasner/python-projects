# Snake Game Part II
Part II of the [Snake Game Part I](https://github.com/sarastrasner/python-projects/tree/main/snakeGame) build. 
Creates and updates a scoreboard and detects collisions with food, wall or tail. Built using Object-Oriented Programming and class inheritance. 

![Snake Game Part 2](https://media.giphy.com/media/bhQfYp2ZGoy0mzhJ1S/giphy.gif)

## Feature Tasks
1. Detect collision with food.
   1. Food is a little blue circle.
   1. Every time the snake touches the food, it moves to a new random spot.
1. Create a scoreboard. 
   1. Keep track of how many pieces of food the snake has eaten.
   1. Display scoreboard at the top.
1. Detect collision with wall.
   1. Use game board coordinates.
   1. If a collision, trigger game over. 
1. Detect collision with tail.
   1. Loop over snake segments and use .distance() to detect a collision to any segment.
   1. If a collision, trigger game over. 
