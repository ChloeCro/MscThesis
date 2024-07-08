import os

LEGAL_TOPIC_LIST = ['feiten en omstandigheden', 'eerdere juridische acties en beslissingen (tevens onderscheid tussen gedaagde, appellant en de verschillende juridische instanties zoals rechtbank, hof van beroep etc.)', 
                    'standpunten van appellant', 'standpunten van verweerder', 'juridische middelen', 'beoordeling door rechter/College', 'proceskosten'] # add topics from doc by gijs'

##### COLUMN CONSTANTS #####
PROCESVERLOOP_COL = 'procesverloop'
OVERWEGINGEN_COL = 'overwegingen'
BESLISSING_COL = 'beslissing'
SECTIONS_COL = 'sections'
ORGANIZED_COL = 'organized'
OLLAMA_COL = 'ollama'
SUMM_COL = 'summary'


##### FILE CONSTANTS #####
# Dataset creation
DATASET_DIR = os.path.abspath(os.path.join('Dataset'))
METADATA_DIR = os.path.join(DATASET_DIR, 'Metadata')
RAW_DIR = os.path.join(DATASET_DIR, 'Raw', '{year}') 
METADATA_PATH = os.path.join(METADATA_DIR, '{year}_rs_data.csv') 
COMBINED_PATH = os.path.join(METADATA_DIR, 'combined.csv')
SUBSET_PATH = os.path.join(METADATA_DIR, 'subset.csv')
COMBINED_SECTION_PATH = os.path.join(METADATA_DIR, 'combined_section.csv')
SUBSET_SECTION_PATH = os.path.join(METADATA_DIR, 'subset_section.csv')
MERGE_PATTERNS_PATH = os.path.join(DATASET_DIR, 'Creation', 'merge_patterns.txt')
SPLIT_PATTERNS_PATH = os.path.join(DATASET_DIR, 'Creation', 'split_patterns.txt')
SECTION_DATA_PATH = os.path.join(DATASET_DIR, 'Creation', 'sectioned_data.csv')

# Prompts
SECTIONING_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Sectioning'))
OLLAMA_SYS_PROMPT_PATH = os.path.join(SECTIONING_DIR, 'Ollama', 'system_prompt.txt')
OLLAMA_PROMPT_PATH = os.path.join(SECTIONING_DIR, 'Ollama', 'prompt.txt')
OLLAMA_PROMPT_NL_PATH = os.path.join(SECTIONING_DIR, 'Ollama', 'prompt_nl.txt')
OLLAMA_SUMM_PROMPT_NL_PATH = os.path.join(SECTIONING_DIR, 'Ollama', 'prompt_summ_nl.txt')
GPT_PROMPT_PATH = os.path.join(SECTIONING_DIR, 'GPT', 'prompt.txt')
SUMMARIZATION_DIR = os.path.abspath(os.path.join('Summarization'))
SUMM_SYS_PROMPT_PATH = ""
SUMM_PROMPT_NL_PATH = ""

# Results documents
LLAMA3_RESULTS = 'Sectioning/Ollama/Responses/results_ollama.csv'