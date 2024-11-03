import pandas as pd

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['Total_Cyclists'] = df.iloc[:, 2:].sum(axis = 1)

monthly_totals = df.groupby('Month')['Total_Cyclists'].sum()
most_popular_month = monthly_totals.idxmax()
max_cyclists = monthly_totals.max()

print(f'the most popular month: {most_popular_month}')
print(f'number of cyclists in this month: {max_cyclists}')