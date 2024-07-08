import sys, os
import ast
import difflib
import ollama
import argparse
import pandas as pd

# Add the root directory (MscThesis) to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Utils.data_helper import load_df, get_section_dict
from Utils.constants import OLLAMA_SYS_PROMPT_PATH, OLLAMA_SUMM_PROMPT_NL_PATH, SUMM_COL, PROCESVERLOOP_COL, OVERWEGINGEN_COL, BESLISSING_COL, OLLAMA_COL

class OllamaSummarizer():
    """
    This class creates a text sectioning object.
    """

    def __init__(self, model):
        # add parameters and model path
        self.model = model
        self.system_prompt, self.prompt = self.get_system_prompt()
        #self.example_text, self.example_output = self.get_example()
        pass

    def get_system_prompt(self):
        # Load the system prompt
        with open(OLLAMA_SYS_PROMPT_PATH, 'r', encoding='utf-8') as file:
            sys_prompt = file.read()

        with open(OLLAMA_SUMM_PROMPT_NL_PATH, 'r', encoding='utf-8') as file:
            prompt = file.read()
        return sys_prompt, prompt

    def get_response(self, input_text):
        response = ollama.chat(model=self.model, keep_alive=0, options={'temperature': 0.0, 'seed': 42, "top_p": 0.0}, messages=[
            {
                'role': 'system',
                'content': self.system_prompt
            },
            {
                'role': 'user',
                'content': self.prompt + input_text
            },
        ])
        return response
    
if __name__ == '__main__':
    summarizer = OllamaSummarizer('llama3:instruct')
    input_df = load_df('C:\\Users\\Chloe\\Documents\\MaastrichtLaw&Tech\\Thesis\\MscThesis\\Dataset\\Metadata\\subset_split\\Gerecht in eerste aanleg van Curaçao.csv')

    print(input_df)

    legal_body = input_df.iloc[0]['instantie']

    responses = []
    for i, row in enumerate(input_df.itertuples(index=True), start=1):
        if i % 10 == 0:
            print(f"Index: {row.Index}")
            #print(responses[i-1])

        procesverloop = getattr(row, PROCESVERLOOP_COL)
        overwegingen = getattr(row, OVERWEGINGEN_COL)
        beslissing = getattr(row, BESLISSING_COL)
        text = procesverloop + "\n" + overwegingen + "\n" + beslissing
        #print(text)

        resp = summarizer.get_response(text)['message']['content']
        print('response: ', resp)
        responses.append(resp)

        
    input_df[SUMM_COL] = responses

    data = pd.DataFrame(input_df)
    data.to_csv(f'results_ollama_summary_{legal_body}.csv', index=False)
    