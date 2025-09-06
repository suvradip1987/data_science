import os
import pandas as pd

os.system('cls')
print("--------------------------")

data = {
    "student_id": [101, 102, None, 104, 105, 106, 107, None, 109, 110,111],
    "student_name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Julia","Dip"],
    "student_age": [20, 21, 22, 20, 23, 21, None, 20, 24, 23,30],
    "marks": [85, 78, 92, 88, 76, 90, 105, 82, 70, 89,95],
    "sex": ["Female", "M", "M", "M", "F", "M", "F","Female" , "M", "F","M"]
}

df= pd.DataFrame(data)
df["student_age"]= df["student_age"].fillna(df["student_age"].mean())
df["marks"].astype(int)

print(type(df.loc[df["sex"]=="Female","sex"]))
print(type(df["student_age"].fillna(df["student_age"].mean())))
print(df["student_age"].fillna(df["student_age"].mean()))

df.loc[df["sex"]=="Female","sex"]="F"
df.loc[df["marks"]>100,"sex"]="F"

print(df)
