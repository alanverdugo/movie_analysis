#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
import csv

# Open ratings .csv file.
df_ratings = pd.read_csv('./ml-latest/ratings.csv', sep=',')

# Open movies .csv file.
df_movies = pd.read_csv('./ml-latest/movies.csv', sep=',')

# Parse and show a list of all possible genres (just out of curiosity)
movie_genres = df_movies['genres'].str.split('|', expand=True)
genre_list = pd.unique(movie_genres.values.ravel())
print "Possible genres:", genre_list

# Extract the launch year of the movie and add it as another column.
df_movies['year'] = df_movies['title'].str.extract('.*\((.*)\).*', expand=True)

# Group by movieID, then get the average rating for that movie.
# After that, we will add that calculated average to a new column in the 
# movies dataframe (called "average_rating").
df_movies['average_rating'] = df_ratings.groupby(['movieId'])['rating'].mean()\
    .reset_index()['rating']

# Since we will need all the values in the record, let's drop any rows where 
# any values are NaN. For example, some movies do not have any ratings, so that 
# will cause the "average_rating" column to be NaN.
df_movies = df_movies.dropna(axis=0, how='any')

# Get the average ratings, grouped per year.
df_average_rating_per_year = df_movies.groupby(['year'])['average_rating']\
    .mean().reset_index()
# Save it to a CSV file.
df_average_rating_per_year.to_csv('df_average_rating_per_year.csv', 
    index_label='index')

# Get data for the axis
x = df_average_rating_per_year['year']
y = df_average_rating_per_year['average_rating']

# Save lowest and highest launch years (for the graph axis).
beginning_year = int(df_movies['year'].min())
ending_year = int(df_movies['year'].max())
print "Lowest year:", beginning_year
print "Highest year:", ending_year

# Set the plot legends.
plt.ylabel("Average rating (0 to 5)")
plt.xlabel("Launch year")
plt.title("Average movie ratings per year")

# Set the axis.
plt.axis([beginning_year, ending_year, 0, 5])
plt.grid(True)

# Plot.
plt.plot(x,y)

# Add an annotation.
plt.annotate('2014 - Average rating: 2.954125\n(The lowest since 1917)',
    xy=("2014", 2.954125), 
    xytext=("1990", 2.5),
    arrowprops=dict(arrowstyle="->", facecolor='black'),
    )

# Set ticks every 5 years.
ticks = []
for tick in range(beginning_year, ending_year+1, 5):
    ticks.append(tick)
plt.xticks(ticks)

# Show the plot.
plt.show()
plt.close()
