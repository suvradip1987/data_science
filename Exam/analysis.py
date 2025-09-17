import pandas as pd
import os

os.system("cls")

food_delivery_df = pd.read_csv("food_dely.csv")
filtered_df = food_delivery_df[["name", "establishment", "city", "locality",
                                "cuisines", "average_cost_for_two", "price_range", "highlights", "aggregate_rating",
                                "rating_text", "votes" ,"delivery"]]
#print(filtered_df.head(5))
filtered_df.info()
print(filtered_df.isnull().sum())
filtered_df["establishment"]= filtered_df["establishment"].fillna(filtered_df["establishment"].mode()[0]).astype("string")
filtered_df["cuisines"]= filtered_df["cuisines"].fillna(filtered_df["cuisines"].ffill())
filtered_df["highlights"]= filtered_df["highlights"].fillna(filtered_df["highlights"].ffill())
#print(filtered_df.isnull().sum())
print(filtered_df["average_cost_for_two"].describe())
filtered_df.info()