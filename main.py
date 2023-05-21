# File Imports
from turtle import Screen
import snake as s
import scoreboard as sb
from food import Food
import time

# SETTING UP THE SCREEN
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.listen()
screen.tracer(0)

# INTIALIZING SNAKE'S BODY, FOOD AND START PROMPT
prompt = sb.Scoreboard()
prompt.start_prompt()
snake = s.Snake()
food = Food()
screen.update()


def game_start():

    prompt.clear()

    # CREATING INSTANCE OF SCOREBOARD
    scorecard = sb.Scoreboard()

    # SETTING UP THE KEY EVENTS TO CONTROL SNAKE MOVEMENT
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.right, "Right")
    screen.onkeypress(snake.left, "Left")

    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)     # updats screen every 0.1 ms

        snake.move()

        # FOOD COLLISION DETECTION
        if (snake.head.distance(food) < 15):
            food.food_refresh(snake.snake_body)
            scorecard.new_score()
            snake.extend()

        # BODY / WALL COLLISION DETECTION
        game_on = snake.collision()

    # FINAL SCORECARD AFTER GAMEOVER
    scorecard.gameover()


# calls game_start function on pressing enter
screen.onkeypress(game_start, 'Return')


screen.update()
screen.exitonclick()
