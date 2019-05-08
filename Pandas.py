import pandas as pd

df = pd.read_csv('D:\Local_Weather_Data.csv')
print(df)
max_temp = df['HiTemp'].max()
print('Maximum temperature is: ', max_temp)
min_temp = df['HiTemp'].min()
print('Minimum temperature is: ', min_temp)
r = df['DateTime'][df['OutHum'] == 40]
print('Print the date when humidity is 40: \n ', r)
avg_hum = df['OutHum'].mean()
print('Average humidity is: ', avg_hum)


