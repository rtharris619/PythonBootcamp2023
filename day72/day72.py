import pandas as pd
import matplotlib.pyplot as plt


def driver():
    analysis = Analysis()
    # analysis.tail_print()
    # analysis.posts_per_language()
    # analysis.check_date()
    analysis.pivot_on_date()
    analysis.plot_language_popularity()


class Analysis:
    def __init__(self):
        self.df = pd.read_csv('./day72/QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
        self.convert_date()
        self.reshaped_df = None

    def convert_date(self):
        self.df['DATE'] = pd.to_datetime(self.df['DATE'])

    def head_print(self):
        print(self.df.head())

    def tail_print(self):
        print(self.df.tail())

    def shape(self):
        print(self.df.shape)

    def posts_per_language(self):
        value = self.df.groupby('TAG').sum()
        value = value.sort_values('POSTS', ascending=False)
        print(value)

    def check_date(self):
        date = self.df['DATE'][0]
        print(date)
        print(type(date))
        date = pd.to_datetime(date)
        print(type(date))

    def pivot_on_date(self):
        self.reshaped_df = self.df.pivot(index='DATE', columns='TAG', values='POSTS')
        print(self.reshaped_df.head())
        self.reshaped_df.fillna(0, inplace=True)
        print(self.reshaped_df.head())
        print(self.reshaped_df.isna().values.any())

    def plot_language_popularity(self):

        self.reshaped_df = self.reshaped_df.rolling(window=6).mean()

        plt.figure(figsize=(16, 10))
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.xlabel('Date', fontsize=14)
        plt.ylabel('Number of Posts', fontsize=14)
        plt.ylim(0, 35000)

        for column in self.reshaped_df.columns:
            plt.plot(self.reshaped_df.index, self.reshaped_df[column], linewidth=3, label=self.reshaped_df[column].name)

        plt.legend(fontsize=16)
        plt.show()
