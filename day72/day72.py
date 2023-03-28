import pandas as pd
from tabulate import tabulate


def driver():
    analysis = Analysis()
    analysis.head_print()
    analysis.posts_per_language()


class Analysis:
    def __init__(self):
        self.df = pd.read_csv('./day72/QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

    def head_print(self):
        print(tabulate(self.df.head(), headers='keys'))

    def tail_print(self):
        print(tabulate(self.df.tail(), headers='keys'))

    def shape(self):
        print(self.df.shape)

    def posts_per_language(self):
        value = self.df.groupby('TAG').sum()
        print(value)
        