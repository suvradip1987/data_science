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


student_df= pd.DataFrame(data)

print(student_df.info())

good_students_df= student_df[student_df["marks"]>=80]
print(good_students_df["student_name"])