from turtle import Turtle, Screen, colormode
import random


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def day18():
    turtle = Turtle()
    # turtle.shape("turtle")
    turtle.color("blue")

    # draw_spirograph(turtle, 5)

    draw_hirst_like_painting(turtle)

    screen = Screen()
    screen.exitonclick()


def draw_square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)


def draw_dashed_line(turtle):
    for _ in range(20):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()


def draw_shape(turtle: Turtle, num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        turtle.forward(100)
        turtle.right(angle)


def draw_shapes(turtle: Turtle):
    for n in range(3, 11):
        turtle.color(random.choice(colors))
        draw_shape(turtle, n)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


def draw_random_walk(turtle: Turtle):
    directions = [0, 90, 180, 270]
    turtle.pensize(15)
    turtle.speed("fastest")
    colormode(255)

    for _ in range(200):
        turtle.color(random_color())
        turtle.forward(30)
        turtle.setheading(random.choice(directions))


def draw_spirograph(turtle: Turtle, size_of_gap):
    colormode(255)
    turtle.speed("fastest")

    gaps = int(360 / size_of_gap)

    for _ in range(gaps):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)


def extract_image_colors():
    import colorgram
    colorgram_colors = colorgram.extract('./day18/image.jpg', 30)

    rgb_colors = []
    for color in colorgram_colors:
        rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
    print(rgb_colors)


def draw_hirst_like_painting(turtle: Turtle):
    color_list = [(201, 157, 111), (63, 104, 125), (153, 84, 51), (124, 81, 96), (126, 162, 175), (133, 173, 160), (187, 140, 47), (182, 135, 147), (222, 198, 133), (46, 31, 18), (185, 92, 110), (64, 125, 113), (19, 44, 56), (60, 159, 129), (201, 96, 81), (147, 24, 37), (229, 172, 164), (10, 22, 20), (46, 26, 32), (86, 144, 161), (144, 33, 24), (29, 76, 89), (222, 175, 183), (104, 127, 157), (163, 208, 193), (50, 64, 80)]

    colormode(255)
    turtle.speed("fastest")

    turtle.penup()
    turtle.hideturtle()

    turtle.setheading(225)
    turtle.forward(300)
    turtle.setheading(0)

    number_of_dots = 100

    for dot_count in range(1, number_of_dots + 1):
        turtle.dot(20, random.choice(color_list))
        turtle.forward(50)

        if dot_count % 10 == 0:
            turtle.setheading(90)
            turtle.forward(50)
            turtle.setheading(180)
            turtle.forward(500)
            turtle.setheading(0)
