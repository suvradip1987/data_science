import numpy as np
import pandas as pd
import os

os.system("cls")
print("----------------------------------------------")

# read data
food_df = pd.read_csv("food_dely.csv")

# Inspect basic info
# food_df.head(100)
# food_df.info()
# print(food_df.isnull().sum())

# handle missing value
food_df["establishment"] = food_df["establishment"].fillna(
    food_df["establishment"].mode()[0]).astype("string")
food_df["cuisines"] = food_df["cuisines"].fillna(
    food_df["cuisines"].ffill())
food_df["highlights"] = food_df["highlights"].fillna(
    food_df["highlights"].ffill())
food_df["name"] = food_df["name"].astype("string")
food_df["city"] = food_df["name"].astype("string")
food_df['cuisines'] = food_df['cuisines'].apply(
    lambda x: [c.strip() for c in x.split(',')])
food_df.rename(columns={'country_id': 'country'}, inplace=True)
food_df['country'] = food_df['country'].map({1: "India"}).astype("string")


# For price_range 1 setting the average_cost_for_two to 50, if average_cost_for_two is < 20

subset_prev = food_df.loc[(food_df["price_range"] == 1) & (
    food_df["average_cost_for_two"] < 20), ["average_cost_for_two","res_id"]]

#print(subset_prev.shape[0])

food_df.loc[(food_df["price_range"] == 1) & (food_df["average_cost_for_two"] <= 20),"average_cost_for_two"]=50

subset_post = food_df.loc[(food_df["price_range"] == 1) & (
    food_df["average_cost_for_two"] < 20), ["average_cost_for_two","res_id"]]


#print(subset_post.shape[0])

print(food_df['aggregate_rating'].describe())
food_df['aggregate_rating'] = food_df['aggregate_rating'].replace(0, np.nan)
food_df['aggregate_rating'] = food_df['aggregate_rating'].fillna(food_df['aggregate_rating'].mean())
print(food_df['aggregate_rating'].describe())

# divide 