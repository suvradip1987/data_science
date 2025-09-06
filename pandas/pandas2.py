import os
import pandas as pd

os.system('cls')
print("--------------------------")

data = {
    "student_id": [101, 102,None,104,105, 106, 107,None, 109, 110,111],
    "student_name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Julia","Dip"],
    "student_age": [20, 21, 22, 20, 23, 21, 45, 20, 24, 23,30],
    "marks": [85, 78, 92, 88, 76, 90, 95, 82, 70, 89,95],
    "sex": ["F", "M", "M", "M", "F", "M", "F",None , "M", "F","M"]
}

df= pd.DataFrame(data)
print(df.isnull())
print(df.isnull().sum())
print(df.dtypes)
print(df.info())

#print(df["student_id"].isnull())
#print(df.loc[df["student_id"].isnull(),"student_name"])
#print(df[df["student_id"].isnull()])
#print(df.loc[df["student_id"].isnull(),"student_id"].fillna("N/A"))
#df.loc[df["student_id"].isnull(),"student_id"]=15
df["student_id"].fillna(15,inplace=True)
df['student_id'] = df['student_id'].astype(int)
print(df.loc[(df["student_age"]>20) & (df["student_age"]<30),"student_id"])
print(df)
