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

# rating_df = pd.read_csv(r'data/archive/rating.csv')
# movie_df = pd.read_csv(r'data/archive/movie.csv')

movie_df=pd.read_csv(r'https://www.kaggle.com/datasets/shubhammehta21/movie-lens-small-latest-dataset?select=movies.csv',  on_bad_lines='skip')
print(movie_df.shape)
print(movie_df.head(10))
