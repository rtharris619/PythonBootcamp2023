import day20.snake as snake
from turtle import Screen
import time


def day20():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    my_snake = snake.Snake()

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

    screen.exitonclick()

















