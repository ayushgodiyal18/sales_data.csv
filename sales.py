import pandas as pd
import matplotlib.pyplot as plt

# Load sales dataset
data = pd.read_csv("sales_big_data.csv")

# Show first 5 rows
print("Dataset Preview:")
print(data.head())

# Total sales by product
product_sales = data.groupby("Product")["Sales_Amount"].sum()
print("\nTotal Sales by Product:")
print(product_sales)

# Total sales by region
region_sales = data.groupby("Region")["Sales_Amount"].sum()
print("\nTotal Sales by Region:")
print(region_sales)

# Average sales
avg_sales = data["Sales_Amount"].mean()
print("\nAverage Sales Amount:", avg_sales)

# Visualization: Product Sales
product_sales.plot(kind="bar")

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales Amount")
plt.show()
