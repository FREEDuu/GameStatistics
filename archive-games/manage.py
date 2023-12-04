import pandas as p
import matplotlib.pyplot as mpl

def cutMonth(str):

    return str.split(' ')[0]


def cutYear(str):
    str = str[-4:]
    return int(str)

dataframe = p.read_csv('video_games.csv')
year = dataframe['release_date']
monthperyear = year
year = year.apply(cutYear)
year_games = dataframe
year_games['release_date'] = year
yearEx = list(set(year))
months_per_year = year_games
count_platform = (dataframe.groupby(['platform'])['name'].count())
count_platform = count_platform.to_frame()
count_platform.columns = ['number of games']
rating_games = (dataframe.groupby(['user_review'])['name'].count())
rating_games = rating_games.to_frame()
rating_games.columns = ['game with this rate']
year_games = year_games.groupby(['release_date'])['name'].count()
year_games = year_games.to_frame()
year_games.columns = ['number of games released']
monthperyear = monthperyear.apply(cutMonth)
months_per_year = dataframe
months_per_year['monthes'] = monthperyear

print(months_per_year)


'''
print(count_platform.rename('count'))

mpl.figure(200)
mpl.barh(count_platform.index, count_platform)
mpl.figure(300)
mpl.barh(rating_games.index, rating_games)
mpl.show()
'''