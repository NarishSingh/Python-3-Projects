# Data science with pandas workshop
# Date created: 12-21-21
# Last Modified: 12-21-20
import matplotlib.pyplot as matplot
import pandas as pd

# Series == columns of data
# if you don't define an idx, it will generate one from 0
series = pd.Series(['Coast Redwood', 'Yellow Meranti', 'Mountain Ash', 'Coast Douglas Fir', 'Sitka Spruce'])
series.index = (['a', 'b', 'c', 'd', 'e'])

# Uses named idx
series2 = pd.Series({'a': 380.3, 'b': 331, 'c': 329.7, 'd': 327, 'e': 317})

print(series)
print(series2)

# Dataframes = tables
df = pd.DataFrame(index=['a', 'b', 'c', 'd', 'e'],
                  data={
                      'name': ['Coast Redwood', 'Yellow Meranti', 'Mountain Ash', 'Coast Douglas Fir', 'Sitka Spruce'],
                      'height': [380.3, 331, 329.7, 327, 317]
                  })

# Importing from the series we created
# df = pd.DataFrame({'name': series, 'height': series2})

# Import from CSV
dfTitantic = pd.read_csv('./titantic.csv')
pd.set_option('display.max_rows', None)  # allows terminal to print the entire things

# Drop null records from columns
# inplace means modify the original dataframe
dfTitantic.dropna(inplace=True)

# Drop entire columns
dfTitantic.drop(['Embarked'], inplace=True, axis='columns')

# .reset_index to reindex the modified set
dfTitantic.reset_index(inplace=True)

# dfTitantic.drop(['Index'], inplace=True, axis='columns')

print(dfTitantic)

# print only the men
print(dfTitantic[dfTitantic['Sex'] == 'male'])

first = dfTitantic[dfTitantic['Pclass'] == 1].reset_index()
print(first)

print(dfTitantic.nlargest(100, 'Fare'))

print(dfTitantic.groupby(['Pclass']).count())

print(dfTitantic.groupby(['Pclass'])['PassengerId'].count())

print(dfTitantic.groupby(['Pclass']).mean())

print(dfTitantic.groupby(['Pclass', 'Sex'])['Survived'].mean())

# matplot for data visualization
dfTitantic.hist(column='Age', by='Pclass')
dfTitantic.plot.scatter(x='Pclass', y='Fare')
dfTitantic.plot.scatter(x='Age', y='Fare')
matplot.show()

dfWeather = pd.read_csv('./weather.csv')
dfWeather.dropna(inplace=True)
dfWeather.reset_index(inplace=True)
dfWeather.drop('index', inplace=True, axis='columns')

dfWeather.plot.line(x='datetime', y='station_london')

matplot.show()
