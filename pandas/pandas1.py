import os
import random
import pandas as pd



os.system('cls')
print("--------------------------")

data = {
    "student_id": [101, 102, None, 104, 105, 106, 107, None, 109, 110,111],
    "student_name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Julia","Dip"],
    "student_age": [20, 21, 22, 20, 23, 21, None, 20, 24, 23,30],
    "marks": [85, 78, 92, 88, 76, 90, 95, 82, 70, 89,95],
    "sex": ["F", "M", "M", "M", "F", "M", "F",None , "M", "F","M"]
}

df = pd.DataFrame(data)

subset_data= df.loc[df["sex"] =="M",["student_id","student_name","student_age"]]
print(subset_data)

for item in df.loc[df["student_id"].isna()].index:
    df.loc[item,"student_id"] = random.randint(150,160)

print(df)


#print(df.head(df.shape[0]))
#print(f"Shape of the data frame is : {df.shape}")
#print(df.isnull().sum())

#df["student_age"]= df["student_age"].fillna(df["student_age"].mean())
#print(df.isnull().sum())
#df.loc[df["student_id"].isna().index[7],"student_id"]=420
#df.loc[7,"student_id"]=430
#print(df)
#print(df["sex"].isna().index)
#print(df["sex"].isna()==True)
#df.loc[7,"sex"]="M"
#df.loc[df["sex"] is None,"sex"]="M"