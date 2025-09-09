import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

os.system("cls")

df_customers = pd.read_csv("Customers.csv")
df_churn = pd.read_csv("Churn.csv")
df_subscriptions = pd.read_csv("Subscriptions.csv")
df_transactions = pd.read_csv("Transactions.csv")

na_customers= df_customers.loc[df_customers["Region"]=="North America"]
print(na_customers.shape[0])

# eu_asia_customers= df_customers.loc[(df_customers["Region"]=="Europe") | (df_customers["Region"]=="Asia")]
countries =["Europe","Asia"]
eu_asia_customers= df_customers.loc[df_customers["Region"].isin(countries)]
print(eu_asia_customers.shape[0])

df_active_customers = df_customers.loc[df_customers["Status"] == "Active"]
print(df_active_customers.shape[0])