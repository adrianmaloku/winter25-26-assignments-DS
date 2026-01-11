import pandas as pd


# Part 1: Reading and inspecting data

df = pd.read_csv('global_sales.csv')

print("=" * 80)
print("PART 1: Reading and Inspecting Data")
print("=" * 80)
print("\nFirst 5 rows:")
print(df.head())
print("\nData types of all columns:")
print(df.dtypes)


# Part 2: Data Cleaning and Indexing

print("\n" + "=" * 80)
print("PART 2: Data Cleaning and Indexing")
print("=" * 80)

print("\n1. Handling Missing Values:")
print(f"Missing values in Units_Sold before filling: {df['Units_Sold'].isna().sum()}")
units_mean = df['Units_Sold'].mean()
df['Units_Sold'] = df['Units_Sold'].fillna(units_mean)
print(f"Missing values in Units_Sold after filling: {df['Units_Sold'].isna().sum()}")

print("\n2. Data Type Casting:")
print(f"Sales column dtype before: {df['Sales'].dtype}")
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Sales'] = df['Sales'].fillna(0)
print(f"Sales column dtype after: {df['Sales'].dtype}")
print(f"Missing values in Sales after conversion: {df['Sales'].isna().sum()}")

print("\n3. Casting Dates:")
print(f"Date column dtype before: {df['Date'].dtype}")
df['Date'] = pd.to_datetime(df['Date'])
print(f"Date column dtype after: {df['Date'].dtype}")

print("\n4. Setting OrderID as index:")
df = df.set_index('OrderID')
print("DataFrame with OrderID as index:")
print(df.head())


print("\n5. Resetting index and setting Date as index:")
df = df.reset_index()
df = df.set_index('Date')
print("DataFrame with Date as index:")
print(df.head())


# Part 3: Filtering, Modifying, and Sorting

print("\n" + "=" * 80)
print("PART 3: Filtering, Modifying, and Sorting")
print("=" * 80)

print("\n1. Filtering Data:")
high_value_sales = df[(df['Sales'] > 500) & (df['Region'] == 'Europe')]
print("high_value_sales DataFrame (Sales > 500 AND Region == 'Europe'):")
print(high_value_sales.head())

print("\n2. Updating and Adding Columns:")
df_reset = df.reset_index()
print(f"Units_Sold value for 5th row (index 4) before update: {df_reset.loc[4, 'Units_Sold']}")
df_reset.loc[4, 'Units_Sold'] = 99
print(f"Units_Sold value for 5th row (index 4) after update: {df_reset.loc[4, 'Units_Sold']}")

df = df_reset.set_index('Date')

df['Profit'] = df['Sales'] * 0.20
print("\nAdded Profit column (Sales * 0.20):")
print(df.head())

print("\n3. Sorting Data:")
df_sorted = df.sort_values(by=['Region', 'Sales'], ascending=[True, False])
print("DataFrame sorted by Region (ascending) and Sales (descending):")
print(df_sorted.head())


# Part 4: Grouping and Aggregation (Analysis)

print("\n" + "=" * 80)
print("PART 4: Grouping and Aggregation (Analysis)")
print("=" * 80)

print("\n1. Regional Performance:")
regional_analysis = df.groupby('Region').agg({
    'Sales': 'sum',
    'Units_Sold': 'mean'
})
print("Total Sales and Average Units_Sold by Region:")
print(regional_analysis)

print("\n2. Product Deep Dive:")
product_profit = df.groupby('Product')['Profit'].max()
print("Maximum Profit by Product:")
print(product_profit)

print("\n3. Time Series Analysis (Monthly Total Sales):")
monthly_sales = df['Sales'].resample('ME').sum()
print("Monthly Total Sales:")
print(monthly_sales)

