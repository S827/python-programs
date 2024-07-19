'''
Perform exploratory data analysis on the netflix_data.csv data to understand more about movies from the 1990s decade.

What was the most frequent movie duration in the 1990s? Save an approximate answer as an integer called duration.

A movie is considered short if it is less than 90 minutes. Count the number of short action movies released in the 1990s 

and save this integer as short_movie_count.

Feel free to experiment after submitting the project!
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

netflix_df = pd.read_csv('./netflix_data.csv')
netflix_df.head()