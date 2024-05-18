

##### COLUMN CONSTANTS #####
PROCESVERLOOP_COL = 'procesverloop'
OVERWEGINGEN_COL = 'overwegingen'
BESLISSING_COL = 'beslissing'
SECTIONS_COL = 'sections'


##### FILE CONSTANTS #####
# Dataset creation
RAW_DIR = 'Dataset/Raw/{year}'
METADATA_PATH = 'Dataset/Metadata/{year}_rs_data.csv'
COMBINED_PATH = 'Dataset/Metadata/combined.csv'
SUBSET_PATH = 'Dataset/Metadata/subset.csv'
MERGE_PATTERNS_PATH = 'Dataset/Creation/merge_patterns.txt'
SPLIT_PATTERNS_PATH = 'Dataset/Creation/split_patterns.txt'
SECTION_DATA_PATH = 'Dataset/Creation/sectioned_data.csv'

# Prompts
OLLAMA_SYS_PROMPT_PATH = 'Sectioning/Ollama/system_prompt.txt'
OLLAMA_PROMPT_PATH = 'Sectioning/Ollama/prompt.txt'
OLLAMA_PROMPT_NL_PATH = 'Sectioning/Ollama/prompt_nl.txt'
GPT_PROMPT_PATH = 'Sectioning/GPT/prompt.txt'