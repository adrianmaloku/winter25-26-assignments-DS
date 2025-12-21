import numpy as np
import pandas as pd

# part 1
product_ids = np.array([1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010])

inventory_data = np.array([
    [50, 15.5, 10.99],
    [120, 3.2, 50.50],
    [30, 25.0, 5.00],
    [75, 12.3, 8.75],
    [90, 7.8, 15.25],
    [45, 18.5, 12.00],
    [110, 4.5, 22.50],
    [60, 20.0, 9.99],
    [85, 10.2, 18.75],
    [95, 14.7, 11.50]
])

print(inventory_data.shape)
print(inventory_data.dtype)

total_value = inventory_data[:, 0] * inventory_data[:, 2]
print(total_value)

products_3_to_7 = inventory_data[3:8]
print(products_3_to_7)

avg_weekly_sales = np.mean(inventory_data[:, 1])
print(avg_weekly_sales)

unit_cost_product_0 = inventory_data[0, 2]
print(unit_cost_product_0)


# part 2
weeks_of_stock = inventory_data[:, 0] / inventory_data[:, 1]
low_stock_mask = weeks_of_stock < 4
low_stock_products = inventory_data[low_stock_mask]
print(low_stock_products)


reorder_quantity = (4 * inventory_data[:, 1]) - inventory_data[:, 0]
reorder_quantity = np.maximum(reorder_quantity, 0)
reorder_quantity = reorder_quantity.reshape(10, 1)
concatenated = np.concatenate([inventory_data, reorder_quantity], axis=1)
print(concatenated)

# part 3
df = pd.DataFrame(concatenated, columns=['Stock', 'Sales', 'Cost', 'Reorder Qty'])
print(df[['Stock', 'Reorder Qty']])
print(df.head(5))
