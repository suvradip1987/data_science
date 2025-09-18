import pandas as pd
import os

os.system("cls")
print("-----------------------------------------------------------")


def get_plan_id(row):
    if row["Type"] == "Deliverable":
        part_before_colon = row["Parent"].split(":")[0]
        number = part_before_colon.strip("#")
    else:
        number = row["Id"]
    return number


program_df = pd.read_csv("AJ21-D4 Launch 1 NS.csv",
                         encoding='utf-16', delimiter='\t')
program_df["Extracted_Parent"] = program_df.apply(get_plan_id, axis=1)

new_df = program_df[["Type", "Id", "Summary", "Extracted_Parent"]]
new_df["Extracted_Parent"] = pd.to_numeric(new_df["Extracted_Parent"])

grouped = new_df.groupby("Extracted_Parent")
output_dir = "Grouped_By_Parent"

for plan_id, items in grouped:
    filename = f"{output_dir}/{plan_id}_group.csv"
    items.to_csv(filename, index=False)
