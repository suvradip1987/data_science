import pandas as pd
import os

os.system("cls")

# Sample data
data = {
    'Region': ['North', 'South', 'North', 'East', 'South', 'East', 'North'],
    'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Sales': [250, 300, 150, 400, 200, 100, 350]
}

sales_df = pd.DataFrame(data)

grouped_by_reg = sales_df.groupby(by=['Region',"Salesperson"])
for item in grouped_by_reg:
    print(item)

sum_based_on_region = grouped_by_reg["Sales"].sum()
#here "Region" is the index
print(sum_based_on_region)

# here normal integers are index
new_df= sum_based_on_region.reset_index()
print(new_df)
