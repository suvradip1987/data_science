import pandas as pd
import os

os.system("cls")

program_df = pd.read_csv("AJ21-D4 Launch 1 NS.csv",encoding='utf-16',delimiter='\t')
#print(program_df.head(10))
plans_df= program_df.loc[program_df["Type"]=="APQP",["Type","Id","Summary"]]