import pandas as pd
import os

os.system("cls")

def get_plan_id(row):
    
    # Step 1: Split by colon to isolate the part before it
    part_before_colon = row.split(":")[0]
    
    # Step 2: Remove the '#' and get the number
    number = part_before_colon.strip("#")
    return number

program_df = pd.read_csv("AJ21-D4 Launch 1 NS.csv",encoding='utf-16',delimiter='\t')
#print(program_df.head(10))
plans_df= program_df.loc[program_df["Type"]=="APQP",["Type","Id","Summary"]]
program_df["Extracted_Parent"]= program_df.loc[program_df["Type"]=="Deliverable","Parent"].apply(get_plan_id)
print(program_df[["Type","Id","Extracted_Parent"]].head(50))
