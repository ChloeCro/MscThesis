import sys, os
import ast
import pandas as pd

# Add the root directory (MscThesis) to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Utils.constants import LLAMA3_RESULTS

##########
# RUN
##########

df = pd.read_csv('C:\\Users\\Chloe\\Documents\\MaastrichtLaw&Tech\\Thesis\\MscThesis\\results_ollama.csv')
output_df = pd.DataFrame(columns=['feiten', 'acties', 'appellant', 'verweerder', 'middelen', 'beoordeling'])
print(df)

# Convert the 'ollama' column in df from string to dictionary
df['ollama'] = df['ollama'].apply(ast.literal_eval)

dictionaries = df['ollama'].tolist()
ids = df['ecli'].tolist()

# Initialize an empty list to store the processed dictionaries
processed_dicts = []

for d, row_id in zip(dictionaries, ids):
    print(d, row_id)
    processed_row = {'id_from_df': row_id}
    text_list = []

    # Iterate over each key-value pair in the dictionary
    for key, nested_dict in d.items():
        # Extract the text from the nested dictionary
        text_value = nested_dict['text']
        
        # Add the text value to the text_list
        text_list.append(text_value)
        
    # Add the text_list to processed_row
    processed_row['text'] = text_list
    
    # Append the processed row dictionary to the list
    processed_dicts.append(processed_row)

# Print the processed dictionaries
for row in processed_dicts:
    print(row)

# Create a DataFrame with the new processed data
resulting_df = pd.DataFrame(processed_dicts)

# Save the resulting DataFrame to a CSV file
resulting_df.to_csv('ollama_processed_impr.csv', index=False)