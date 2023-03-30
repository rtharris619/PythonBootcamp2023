import pandas as pd
import matplotlib.pyplot as plt


def driver():
    analysis = Analysis()
    # analysis.sets_for_year(1949)
    # analysis.sets_by_year()
    analysis.themes_by_year()


class Analysis:
    def __init__(self):
        self.colors_df = pd.read_csv('./day73/data/colors.csv')
        self.sets_df = pd.read_csv('./day73/data/sets.csv')

    def colors_print(self):
        print(self.colors_df.head())

    def num_unique_colors(self):
        print(self.colors_df['name'].nunique())

    def num_transparent_colors(self):
        # print(self.colors_df.groupby('is_trans').count())
        print(self.colors_df['is_trans'].value_counts())

    def sets_print(self):
        print(self.sets_df.head())

    def sets_sorted_by_year(self):
        print(self.sets_df.sort_values('year').head())

    def sets_for_year(self, year):
        print(self.sets_df[self.sets_df['year'] == year])

    def sets_with_most_parts(self):
        print(self.sets_df.sort_values('num_parts', ascending=False).head(10))

    def sets_by_year(self):
        temp = self.sets_df.groupby('year').count().sort_values('year')
        print(temp['set_num'].head())
        print(temp['set_num'].tail())

    def plot_sets_by_year(self):
        sets_by_year_df = self.sets_df.groupby('year').count().sort_values('year')
        sets_by_year_df = sets_by_year_df.rolling(window=6).mean()
        plt.plot(sets_by_year_df.index[:-2], sets_by_year_df['set_num'][:-2])
        plt.show()

    def themes_by_year(self):
        themes_by_year_df = self.sets_df.groupby('year').agg({'theme_id': pd.Series.nunique}).sort_values('year')
        themes_by_year_df.rename(columns={'theme_id': 'nr_themes'}, inplace=True)
        print(themes_by_year_df.head())
        plt.plot(themes_by_year_df.index[:-2], themes_by_year_df['nr_themes'][:-2])
        plt.show()
