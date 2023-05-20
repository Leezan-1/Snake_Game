# File Imports
from turtle import Screen
import snake as s
import scoreboard as sb
from food import Food
import time

# TODO : setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.listen()
screen.tracer(0)

# Creating instances of snake, food and scorecard
snake = s.Snake()
food = Food()
scorecard = sb.Scoreboard()
screen.update()

# TODO : SETTING UP THE KEY EVENTS TO CONTROL SNAKE MOVEMENT
game_on = True
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.left, "Left")

# LOOPING THROUGH THE GAME
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Food collision detection
    if (snake.head.distance(food) < 15):
        food.food_refresh(snake.snake_body)
        scorecard.new_score()
        snake.extend()

    # checks snake's collision with the body or wall
    game_on = snake.collision()

# FINAL SCORECARD AFTER GAMEOVER
scorecard.gameover()
screen.update()
screen.exitonclick()
