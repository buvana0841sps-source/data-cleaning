import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("retail_data.csv")

df = df.dropna()
df = df.drop_duplicates()
df['TransactionTime'] = pd.to_datetime(df['TransactionTime'])
df = df[df['Quantity'] > 0]

df['TotalSales'] = df['Quantity'] * df['CostPerItem']
df['Month'] = df['TransactionTime'].dt.month
df['Year'] = df['TransactionTime'].dt.year

top_products = df.groupby('ItemDescription')['TotalSales'].sum().sort_values(ascending=False).head(10)
monthly_sales = df.groupby('Month')['TotalSales'].sum()
country_sales = df.groupby('Country')['TotalSales'].sum().sort_values(ascending=False)

print(top_products)
print(monthly_sales)
print(country_sales)

monthly_sales.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.show()

top_products.plot(kind='bar')
plt.title("Top Products")
plt.show()
