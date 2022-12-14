import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import re
import os


import warnings
warnings.filterwarnings('ignore')

plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = [18, 8]


rating_df = pd.read_csv(r'../data/ml-20m/ratings.csv', dtype={'timestamp':'datetime'})
#
# movie_df = pd.read_csv(r'../data/ml-20m/movies.csv')

# rating_df = pd.read_csv(r'../data/ml-20m/ratings_2.csv', parse_dates=['timestamp'], dtype={'userId': 'uint32', 'movieId': 'uint32', 'rating': 'float32'})
# movie_df = pd.read_csv(r'../data/ml-20m/movies.csv', dtype={'movieId': 'uint32'})
if __name__ == '__main__':
    # rating_df['gave_rating_year'] = rating_df['timestamp']
    print(rating_df.shape)
    print(rating_df.head(3))

    # print(movie_df.shape)
    # print(movie_df.head(3))
