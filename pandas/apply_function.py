from os import system
import pandas as pd

system("cls")

data = [
    {"id": 101, "name": "Alice", "age": 20, "marks": 85},
    {"id": 102, "name": "Bob", "age": 21, "marks": 90},
    {"id": 103, "name": "Charlie", "age": 19, "marks": None},
    {"id": 104, "name": "David", "age": 22, "marks": 88}
]

df = pd.DataFrame(data)
df["marks"]= df["marks"].fillna(df["marks"].mean())

def grade(marks):
    if pd.isna(marks):
        return "Incomplete"
    elif marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    else:
        return "C"

df['grade'] = df['marks'].apply(grade)
#df['grade'] = df['marks'].apply(lambda mark: grade(mark)) # this also works
print(df)