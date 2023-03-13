from turtle import Turtle, Screen
import random


class Tim:
    def __init__(self):
        self.tim = Turtle()
        self.screen = Screen()
        self.screen.listen()
        self.screen.onkey(self.move_forwards, "w")
        self.screen.onkey(self.move_backwards, "s")
        self.screen.onkey(self.move_left, "a")
        self.screen.onkey(self.move_right, "d")
        self.screen.onkey(self.clear, "c")
        self.screen.exitonclick()

    def move_forwards(self):
        self.tim.forward(10)

    def move_backwards(self):
        self.tim.backward(10)

    def move_left(self):
        self.tim.setheading(self.tim.heading() + 10)

    def move_right(self):
        self.tim.setheading(self.tim.heading() - 10)

    def clear(self):
        self.tim.clear()
        self.tim.penup()
        self.tim.home()
        self.tim.pendown()


def etch_a_sketch():
    tim = Tim()


def turtle_racing():

    is_race_on = False

    screen = Screen()
    screen.setup(width=500, height=400)

    bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
    colours = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_positions = [-70, -40, -10, 20, 50, 80]

    turtles = []

    for i in range(0, 6):
        t = Turtle(shape="turtle")
        t.penup()
        t.color(colours[i])
        t.goto(x=-230, y=y_positions[i])
        turtles.append(t)

    if bet:
        is_race_on = True

    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")

            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

    screen.exitonclick()


def day19():
    turtle_racing()



