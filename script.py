import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

#loading data
file_location = 'data/netflix_titles.csv'
data = pd.read_csv(file_location)
data.head()
data.count()

#%%
#number of tv shows vs movies
netflix_shows = data[data['type']=='TV Show']
netflix_movies = data[data['type']=='Movie']
sns.set(style='darkgrid')
ax = sns.countplot(x='type', data=data, palette="bright")

#%%
#Ratings of content --count--
plt.figure(figsize=(12,10))
plt.title("Ratings Count")
sns.set(style='darkgrid')
ax = sns.countplot(x='rating', data = data, palette = 'bright', order=data['rating'].value_counts().index[0:15])

#%%
#Ratings of content --pie--
data['rating'].value_counts().plot.pie(autopct='%1.1f%%',figsize=(20,35))
plt.title("Ratings Percent")
plt.show()

#%%
#Rating of Movies and TV Shows seperated
plt.figure(figsize=(12,8))
plt.title("Ratings of Movies vs TV Shows")
ax = sns.countplot(x='rating', data=data,hue='type', palette='bright')

#%%
plt.figure(figsize=(12,10))
sns.set(style='darkgrid')
ax = sns.countplot(x='country',data = data, palette='bright',order=data['country'].value_counts().index[0:10])

#%%
plt.figure(figsize=(35,6))
plt.title("Year of Release")
sns.countplot(x='release_year', data = data)

#%%
#popular genres of tv shows
plt.figure(figsize=(12,6))
plt.title("Top 10 Genres of TV Shows")
data[data['type']=='TV Show']['listed_in'].value_counts()[:10].plot(kind='barh',color='red')

#%%
#popular genres of movies
plt.figure(figsize=(12,6))
data[data["type"]=="Movie"]["listed_in"].value_counts()[:10].plot(kind="barh",color="red")
plt.title("Top 10 Genres of Movies")

#%%
#common runtimes for movies
plt.figure(figsize=(35,6))
plt.title("25 Most Common Runtimes for Movies", size=18)
ax = sns.countplot(x='duration',data = netflix_movies,palette = 'bright', order=netflix_movies['duration'].value_counts().index[:25])

#%%
#Common durations for TV Shows
plt.figure(figsize=(35,6))
plt.title("25 Most Common Durations of TV Shows", size=18)
ax = sns.countplot(x='duration', data=netflix_shows, palette='Spectral', order=netflix_shows['duration'].value_counts().index[:])

#%%
plt.figure(figsize=(15,7))
title_and_duration=['title','duration']
durations= netflix_shows[title_and_duration]
#get rid of season
durations['no_of_seasons']=durations['duration'].str.replace(' Season','')
#seasons
durations['no_of_seasons']=durations['no_of_seasons'].str.replace('s','')
#convert season count into int type
durations['no_of_seasons']=durations['no_of_seasons'].astype(str).astype(int)
#-----------------------------------------------------------------------
long_dur_index = ['title','no_of_seasons']
longest_running = durations[long_dur_index]
longest_running = longest_running.sort_values(by='no_of_seasons',ascending=False)
top_longest = longest_running[:15]
top_longest.plot(kind='barh',x='title',y='no_of_seasons',color='red')
plt.title("TV Shows with Most Seasons (Top 15)")

