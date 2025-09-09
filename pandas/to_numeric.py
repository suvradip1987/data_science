import pandas as pd
import numpy as np
import os

os.system("cls")

# Sample data
df = pd.DataFrame({
    'customer_id': [101, 102, 103, 104],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'marks': ['85', 'NaN', 'invalid', 92]
})


df.info()

df["marks"]= pd.to_numeric(df["marks"], errors="coerce")
df.info()