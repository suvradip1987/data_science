import pandas as pd
import os

os.system("cls")

data = {
    "student_id": [101, 102, None, 104, 105, 106, 107, None, 109, 110,111],
    "student_name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Julia","Dip"],
    "student_age": [20, 21, 22, 20, 23, 21, None, 20, 24, 23,30],
    "marks": [85, 78, 92, 88, 76, 90, 105, 82, 70, 89,95],
    "sex": ["Female", "M", "M", "M", "F", "M", "F","Female" , "M", "F","M"]
}

strudent_df= pd.DataFrame(data)

for col_name in strudent_df.columns:
    print(f"Column Name {col_name}")

for index,row in strudent_df.iterrows():
    print(f"Index is {index} and Student Name is {row['student_name']}")