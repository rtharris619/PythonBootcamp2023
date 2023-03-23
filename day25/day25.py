import pandas


def day_25():
    states_game()


def read_csv():
    import csv
    with open("./day25/weather_data.csv") as data_file:
        data = csv.reader(data_file)
        temperatures = []
        for row in data:
            if row[1] != "temp":
                temperatures.append(int(row[1]))

        print(temperatures)


def read_csv_with_pandas():
    data = pandas.read_csv("./day25/weather_data.csv")
    data_dict = data.to_dict()
    print(data_dict)

    temp_list = data['temp'].to_list()
    print(temp_list)

    mean = data['temp'].mean()
    print(mean)

    monday = data[data.day == 'Monday']
    print(monday.temp)

    max_temp_row = data[data.temp == data.temp.max()]
    print(max_temp_row)


def create_dataframe():
    data_dict = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }

    data = pandas.DataFrame(data_dict)
    # data.to_csv("./day25/new_data.csv")


def read_squirrel_data():
    data = pandas.read_csv("./day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

    gray_count = len(data[data['Primary Fur Color'] == 'Gray'])
    red_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
    black_count = len(data[data['Primary Fur Color'] == 'Black'])

    print(gray_count, red_count, black_count)


def states_game():
    import turtle

    screen = turtle.Screen()
    screen.title('U.S. States Game')
    image = "./day25/blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    data = pandas.read_csv("./day25/50_states.csv")
    all_states = data.state.to_list()
    guessed_states = []

    while len(guessed_states) < 50:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                        prompt="What's another state's name?").title()

        if answer_state == 'Exit':
            missing_states = []
            for state in all_states:
                if state not in guessed_states:
                    missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv('./day25/states_to_learn.csv')
            break

        if answer_state in all_states:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(state_data.state.item())
            guessed_states.append(state_data.state.item())

    turtle.mainloop()

    screen.exitonclick()
