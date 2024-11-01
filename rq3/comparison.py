import pandas as pd

# Read CSV files
table3 = pd.read_csv('./results/role/table3.csv')
table4 = pd.read_csv('./results/without_role/table4.csv')

# Ensure both tables have the same shape and column order
assert table3.shape == table4.shape, "The tables do not have the same shape."
assert all(table3.columns == table4.columns), "The columns of the tables do not match."
assert all(table3['Attribute'] == table4['Attribute']), "The attributes of the tables do not match."

# Create a new DataFrame to store the results of up or down
comparison_result = table3[['Attribute']].copy()

# Compare each value and fill the results with "down" or "up"
for column in table3.columns[1:]:  # Start from the second column, skipping the "Attribute" column
    comparison_result[column] = ["down" if v4 < v3 else "up" for v3, v4 in zip(table3[column], table4[column])]

# Filter out the "Total" row
comparison_no_total = comparison_result[comparison_result['Attribute'] != 'Total']

# Count the number of "up" and "down"
up_count = (comparison_no_total.iloc[:, 1:] == "up").sum().sum()
down_count = (comparison_no_total.iloc[:, 1:] == "down").sum().sum()

# Output results to the console
print(f"Total 'up' (excluding 'Total' row): {up_count}")
print(f"Total 'down' (excluding 'Total' row): {down_count}")

# Save detailed comparison results to a CSV file
comparison_result.to_csv('./rq3/comparison_result.csv', index=False)
print("Comparison result saved to './comparison_result.csv'")
