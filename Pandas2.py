import pandas as pd

weather_data = {
    'day': ['1/1/2019', '1/2/2019', '1/3/2019', '1/4/2019', '1/5/2019', '1/6/2019'],
    'temperature': [32, 35, 28, 24, 32, 31],
    'wind_speed': [6, 7, 2, 7, 4, 2],
    'event': ['Rain', 'Sunny', 'Snow', 'Snow', 'Rain', 'Sunny']
}
df = pd.DataFrame(weather_data)
print(df)
shape = df.shape
print('Dimension of file: ', shape)
h = df.head(3)   # print few rows of a table
print(h)
t = df.tail(2)
print(t)
print(df.columns)  # show columns
print(df.day)  # show individual column
print(df[['event', 'day']])
print(df.describe())  # prints the statistical data



