import os
import re
import sys
import string
import argparse
import multiprocessing
import pandas as pd
import numpy as np
import datetime
import time
import psutil
import warnings
warnings.filterwarnings("ignore")

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


from datetime import timedelta
from multiprocessing import Pool
from tqdm import tqdm
from functools import partial
from pathlib import Path
from summarizer import Summarizer, TransformerSummarizer

script_dir = Path(__file__).parent
sys.path.append(str(script_dir.parent))

from general_utils.data_helper import get_single_document_list, filter_df, create_csv_from_df, get_text
from general_utils.model_utils import load_model
from summ_pipeline.utils.preprocess_text import remove_info
from summ_pipeline.extractive_methods.graph_based_methods import textRank
from summ_pipeline.extractive_methods.clustering_based_methods import k_means
# from summ_pipeline.extractive_methods.heuristic_based_methods import
from summ_pipeline.extractive_methods.deeplearning_based_methods import bertSum #, gptSum
from summ_pipeline.abstractive_methods.methods import bart
from old.bert_method import bert
#from summ_pipeline.abstractive_methods.methods import bart, t5

df = pd.read_csv("text_topics.csv")

titles = df['name'].tolist()
documents = df['text'].tolist()

print(documents)

results = []
for id,text in enumerate(documents):
    print(text)
    results.append(titles[id])
    result = bart(text)
    print(result)
    results.extend([result])
print(results)
print(' '.join(results))