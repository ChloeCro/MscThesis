import sys, os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Add the MscThesis directory to the Python path
sys.path.append(os.path.abspath(os.path.join('..')))

from Utils.constants import COMBINED_PATH, METADATA_PATH


if __name__ == '__main__':
    # Read individual CSVs
    df1 = pd.read_csv("C:/Users/Chloe/Documents/MaastrichtLaw&Tech/Thesis/MscThesis/Dataset/Metadata/2020_rs_data.csv")
    df2 = pd.read_csv("C:/Users/Chloe/Documents/MaastrichtLaw&Tech/Thesis/MscThesis/Dataset/Metadata/2021_rs_data.csv")
    df3 = pd.read_csv("C:/Users/Chloe/Documents/MaastrichtLaw&Tech/Thesis/MscThesis/Dataset/Metadata/2022_rs_data.csv")

    # Concatenate dataframes vertically
    combined = pd.concat([df1, df2, df3], ignore_index=True)

    combined['year'] = pd.to_datetime(combined['date']).dt.year
    combined.to_csv("C:/Users/Chloe/Documents/MaastrichtLaw&Tech/Thesis/MscThesis/Dataset/Metadata/combined.csv", index=False)

    # Group by 'year' and 'instantie', then count the occurrences
    grouped = combined.groupby(['year', 'instantie']).size().reset_index(name='value')

#
