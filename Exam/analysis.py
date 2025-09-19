import pandas as pd
import os

os.system("cls")
print("----------------------------------------------")

food_df = pd.read_csv("food_dely.csv")
# print(filtered_df.head(5))
print(food_df.isnull().sum())
food_df["establishment"] = food_df["establishment"].fillna(
    food_df["establishment"].mode()[0]).astype("string")
food_df["cuisines"] = food_df["cuisines"].fillna(
    food_df["cuisines"].ffill())
food_df["highlights"] = food_df["highlights"].fillna(
    food_df["highlights"].ffill())
food_df["name"] = food_df["name"].astype("string")
food_df["city"] = food_df["name"].astype("string")
food_df['cuisines'] = food_df['cuisines'].apply(lambda x: [c.strip() for c in x.split(',')])
food_df.rename(columns={'country_id': 'country'}, inplace=True)
food_df['country']= food_df['country'].map({1:"India"}).astype("string")
print(food_df.isnull().sum())
# print(filtered_df.isnull().sum())
print(food_df["average_cost_for_two"].describe())
