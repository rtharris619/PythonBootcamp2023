

def day_25():
    read_csv_with_pandas()


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
    import pandas
    data = pandas.read_csv("./day25/weather_data.csv")
    print(data["temp"])
