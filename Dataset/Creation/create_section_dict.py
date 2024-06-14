# From create_sections resulting csv

import sys, os
import pandas as pd
import argparse
import ast
from collections import defaultdict

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Utils.constants import COMBINED_SECTION_PATH, SUBSET_SECTION_PATH

def organize_by_number(strings):
    result = defaultdict(list)
    for string in strings:
        period_index = string.find('.')
        if period_index != -1:
            number = string[:period_index]
            if number.isdigit():
                result[int(number)].append(string)

    # Join the lists into a single string per key
    for key in result:
        result[key] = ' '.join(result[key])

    # Sort the dictionary by keys to ensure order
    sorted_result = dict(sorted(result.items()))
    return sorted_result

def apply_to_dataframe(df, column_name):
    # Convert string representations of lists to actual lists
    df[column_name] = df[column_name].apply(ast.literal_eval)
    # Apply the organize_by_number function to each row's specified column
    df[column_name] = df[column_name].apply(organize_by_number)
    return df

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Data sectioning script')
    parser.add_argument('--fullset', action='store_true', help='If provided, use the full data CSV file.')
    args = parser.parse_args()

    if args.fullset:
        path = COMBINED_SECTION_PATH
    else:
        path = SUBSET_SECTION_PATH

    # Reading the CSV file
    data = pd.read_csv(path)

    # Applying the function to the DataFrame
    organized_df = apply_to_dataframe(data, 'sections')
    print(organized_df.sections)

    # Saving the processed DataFrame to a new CSV file
    organized_df.to_csv(path, index=False)
