import pandas


def day_25():
    read_squirrel_data()


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
