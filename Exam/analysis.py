import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

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
food_df["city"] = food_df["city"].astype("string")
food_df['cuisines'] = food_df['cuisines'].apply(
    lambda x: [c.strip() for c in x.split(',')])
food_df.rename(columns={'country_id': 'country'}, inplace=True)
food_df['country'] = food_df['country'].map({1: "India"}).astype("string")


# For price_range 1 setting the average_cost_for_two to 50, if average_cost_for_two is < 20
food_df.loc[(food_df["price_range"] == 1) & (
    food_df["average_cost_for_two"] <= 20), "average_cost_for_two"] = 50

#print(food_df['aggregate_rating'].describe())
food_df['aggregate_rating'] = food_df['aggregate_rating'].replace(0, np.nan)
food_df['aggregate_rating'] = food_df['aggregate_rating'].fillna(
    food_df['aggregate_rating'].mean())

# divide region into North, South by latitude
city_to_region = {
    'Agra': 'North',
    'Ahmedabad': 'West',
    'Gandhinagar': 'West',
    'Ajmer': 'North',
    'Alappuzha': 'South',
    'Allahabad': 'North',
    'Amravati': 'West',
    'Amritsar': 'North',
    'Aurangabad': 'West',
    'Bangalore': 'South',
    'Bhopal': 'Central',
    'Bhubaneshwar': 'East',
    'Chandigarh': 'North',
    'Mohali': 'North',
    'Panchkula': 'North',
    'Zirakpur': 'North',
    'Nayagaon': 'North',
    'Chennai': 'South',
    'Coimbatore': 'South',
    'Cuttack': 'East',
    'Darjeeling': 'East',
    'Dehradun': 'North',
    'New Delhi': 'North',
    'Gurgaon': 'North',
    'Noida': 'North',
    'Faridabad': 'North',
    'Ghaziabad': 'North',
    'Greater Noida': 'North',
    'Dharamshala': 'North',
    'Gangtok': 'East',
    'Goa': 'West'}

food_df['region'] = food_df['city'].map(city_to_region)
# If mapping misses some, fill with 'Other'
food_df['region'] = food_df['region'].fillna('Other')

#food_df.to_csv('post_cleaning.csv', index=False)

#Top 10 restaurants by rating
top = food_df.sort_values('aggregate_rating', ascending=False).head(10)
#print(top[['name','city','aggregate_rating','average_cost_for_two','votes']])

# Distribution of price ranges
plt.figure(figsize=(6,4))
sns.countplot(x='price_range', data=food_df)
plt.title('Price Range Distribution')
plt.xlabel('Price Range')
plt.ylabel('Count')
plt.show()

cols = ['average_cost_for_two', 'aggregate_rating', 'votes']
df_corr = food_df[cols].copy()
df_corr['votes'] = food_df['votes'].replace(0, np.nan)
df_corr['votes'] = df_corr['votes'].dropna()

#Compute correlations
pearson_corr = df_corr.corr(method='pearson')
spearman_corr = df_corr.corr(method='spearman')

#Correlation heatmap (Pearson)
plt.figure(figsize=(6,5))
sns.heatmap(pearson_corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Pearson correlation: cost, rating, votes")
plt.tight_layout()
plt.show()

#Correlation heatmap (spearman)
plt.figure(figsize=(6,5))
sns.heatmap(spearman_corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Pearson correlation: cost, rating, votes")
plt.tight_layout()
plt.show()