import day20.snake as snake
import day20.food as food
import day20.scoreboard as scoreboard
from turtle import Screen
import time


def day20():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    my_snake = snake.Snake()
    my_food = food.Food()
    my_scoreboard = scoreboard.Scoreboard()

    screen.listen()
    screen.onkey(my_snake.up, "Up")
    screen.onkey(my_snake.down, "Down")
    screen.onkey(my_snake.left, "Left")
    screen.onkey(my_snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)

        my_snake.move()

        # Detects a collision with the food
        if my_snake.head.distance(my_food) < 15:
            my_food.refresh()
            my_scoreboard.increase_score()

    screen.exitonclick()

















