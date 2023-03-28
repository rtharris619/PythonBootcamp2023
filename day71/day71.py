import pandas as pd
from tabulate import tabulate


def driver():
    analysis = Analysis()
    # analysis.highest_salary_row()
    # analysis.columns_print()
    # analysis.head_print()
    # analysis.lowest_starting_salary()
    # analysis.highest_risk_major()
    # analysis.greatest_salary_spread()
    # analysis.group_mean()
    analysis.group_max()


class Analysis:
    def __init__(self):
        pd.options.display.float_format = '{:,.2f}'.format
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

    def highest_mid_career_salary(self):
        highest = self.df['Mid-Career Median Salary'].max()
        print(highest)

        index = self.df['Mid-Career Median Salary'].idxmax()
        major = self.df['Undergraduate Major'][index]
        print(major)

    def highest_salary_row(self):
        highest_row_index = self.df['Starting Median Salary'].idxmax()
        row = self.df.loc[highest_row_index]
        print(row)

    def lowest_starting_salary(self):
        min_salary = self.df['Starting Median Salary'].min()
        print(min_salary)

        index = self.df['Mid-Career Median Salary'].idxmin()
        major = self.df['Undergraduate Major'][index]
        print(major)

    def lowest_risk_major(self):
        self.insert_spread()

        lowest_risk = self.df.sort_values('Spread')
        print(lowest_risk[['Undergraduate Major', 'Spread']].head())

    def highest_risk_major(self):
        self.insert_spread()

        highest_risk = self.df.sort_values('Spread', ascending=False)
        print(highest_risk[['Undergraduate Major', 'Spread']].head())

    def insert_spread(self):
        spread_col = self.df['Mid-Career 90th Percentile Salary'].subtract(self.df['Mid-Career 10th Percentile Salary'])
        self.df.insert(1, 'Spread', spread_col)

    def greatest_salary_spread(self):
        self.insert_spread()

        highest_potential = self.df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
        print(highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head())

        highest_salary = self.df.sort_values('Mid-Career Median Salary', ascending=False)
        print(highest_salary[['Undergraduate Major', 'Mid-Career Median Salary']].head())

        # biggest_gap = self.df.sort_values('Spread', ascending=False)
        # print(biggest_gap[['Undergraduate Major', 'Spread']].head())

    def group_count(self):
        count = self.df.groupby('Group').count()
        print(count)

    def group_mean(self):
        mean = self.df.groupby('Group')['Mid-Career 90th Percentile Salary'].mean()
        print(mean)

    def group_max(self):
        max_salary_by_group = self.df.groupby('Group')['Mid-Career 90th Percentile Salary'].max()
        print(max_salary_by_group)
