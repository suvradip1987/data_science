import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

os.system("cls")

df_customers = pd.read_csv(
    "C:\\Users\\smondal1\\OneDrive\\OneDrive - JLR\\Desktop\\zomato data\\Customers.csv")
df_churn = pd.read_csv(
    "C:\\Users\\smondal1\\OneDrive\\OneDrive - JLR\\Desktop\\zomato data\\Churn.csv")
df_subscriptions = pd.read_csv(
    "C:\\Users\\smondal1\\OneDrive\\OneDrive - JLR\\Desktop\\zomato data\\Subscriptions.csv")
df_transactions = pd.read_csv(
    "C:\\Users\\smondal1\\OneDrive\\OneDrive - JLR\\Desktop\\zomato data\\Transactions.csv")

print(df_customers.shape)
print(df_churn.shape)
print(df_subscriptions.shape)
print(df_transactions.shape)

print(df_customers[["FirstName", "LastName"]])


for index,row in df_customers.head(10).iterrows():
    print(row["FirstName"])

df_customers_from_northAmria = df_customers.loc[df_customers["Region"]
                                                == "North America", "CustomerID"]

df_customers_from_europeOrAsia = df_customers.loc[(
    df_customers["Region"] == "Europe") | (df_customers["Region"] == "Asia"), "CustomerID"]

# print(df_customers_from_europeOrAsia.shape)

df_active_customers = df_customers.loc[df_customers["Status"]
                                       == "Active", "CustomerID"]
print(df_active_customers.shape[0])

status_counts = df_customers['Status'].value_counts()

# Pie chart setup
plt.figure(figsize=(6, 6))
colors = sns.color_palette('pastel')[0:2]
plt.pie(
    status_counts,
    labels=status_counts.index,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    wedgeprops={'edgecolor': 'black'}
)

plt.title('User Activity Distribution')
plt.tight_layout()
plt.show()
