import pandas as pd
import os

df = pd.read_csv("C:\\Users\\Chloe\\Documents\\MaastrichtLaw&Tech\\Thesis\\MscThesis\\Dataset\\Metadata\\subset_section.csv")

# Column to split by
split_column = 'instantie'

# Directory to save the files
output_dir = 'C:\\Users\\Chloe\\Documents\\MaastrichtLaw&Tech\\Thesis\\MscThesis\\Dataset\\Metadata\\subset_split'

# Create the output directory if it does not exist
os.makedirs(output_dir, exist_ok=True)

# Get unique values in the column
unique_values = df[split_column].unique()

# Create separate CSV files for each unique value
for value in unique_values:
    subset_df = df[df[split_column] == value]
    file_name = f"{value}.csv"
    file_path = os.path.join(output_dir, file_name)
    subset_df.to_csv(file_path, index=False)
    print(f"Saved {file_path}")