import pandas as pd
from tabulate import tabulate


def driver():
    analysis = Analysis()
    # analysis.highest_salary_row()
    analysis.columns_print()


class Analysis:
    def __init__(self):
        self.df = pd.read_csv('./day71/salaries_by_college_major.csv')
        self.clean_up()

    def head_print(self):
        print(tabulate(self.df.head(), headers='keys'))

    def tail_print(self):
        print(tabulate(self.df.tail(), headers='keys'))

    def shape_print(self):
        shape = self.df.shape
        print(shape)

    def columns_print(self):
        columns = self.df.columns
        for col in columns:
            print(col)

    def missing_values_print(self):
        values = self.df.isna()
        print(tabulate(values, headers='keys'))

    def clean_up(self):
        self.df = self.df.dropna()
        # self.tail_print()

    def column_print(self):
        column_data = self.df['Starting Median Salary']
        print(column_data)

    def highest_salary(self):
        highest = self.df['Starting Median Salary'].max()
        print(highest)

    def highest_salary_row(self):
        highest_row_index = self.df['Starting Median Salary'].idxmax()
        row = self.df.loc[highest_row_index]
        print(row)
