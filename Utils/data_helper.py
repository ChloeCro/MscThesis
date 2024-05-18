import pandas as pd
import sys, os
import ast
import re

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Utils.constants import SECTIONS_COL

def get_single_document_list(row):
    """
    (for now) Extracts the texts from the three section columns for each row, 
    combines them and adds them as a full text in a string.

    params:
    row := pandas dataframe row
    """
    procesverloop = str(row['procesverloop'])
    overwegingen = str(row['overwegingen'])
    beslissing = str(row['beslissing'])

    return ' '.join([procesverloop, overwegingen, beslissing])

def get_text(row):
    # For rechtspraak-extractor
    text = str(row['text']) # change column name back to 'fulltext'
    return text


def filter_df(df):
    """
    filtering the dataframe based on rules.
    
    Rules:
    1. Remove rows with no or too short reference summaries (inhoudsindicatie text length <= 15)
    """
    df_filtered = df[df['fulltext'].notna() & (df['fulltext'] != '')]
    df_filtered = df_filtered[df_filtered['inhoudsindicatie'].apply(lambda x: len(x.split(' ') if isinstance(x, str) else '') >= 15)]
    return df_filtered

def load_df(path):
    data = pd.read_csv(path)
    return data

def get_section_dict(row):
    """ Gets section dictionary from dataframe """
    d = row[SECTIONS_COL].apply(ast.literal_eval)
    return d

def create_csv_from_df():
    pass