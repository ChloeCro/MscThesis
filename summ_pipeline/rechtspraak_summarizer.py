import os
import re
import sys
import ast
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

from Utils.data_helper import get_single_document_list, filter_df, create_csv_from_df, get_text
#from Utils.model_utils import load_model
from summ_pipeline.utils.preprocess_text import remove_info
from summ_pipeline.extractive_methods.graph_based_methods import textRank
from summ_pipeline.extractive_methods.clustering_based_methods import k_means
# from summ_pipeline.extractive_methods.heuristic_based_methods import
from summ_pipeline.extractive_methods.deeplearning_based_methods import bertSum #, gptSum
from summ_pipeline.abstractive_methods.methods import bart, llm_summarizer
#from old.bert_method import bert
#from summ_pipeline.abstractive_methods.methods import bart, t5

class RsSummarizer():

    def __init__(self, method):
        self.method = method

    def summarize_text(self, text, param, model=None):
        # result should be list of sentences!
        result = []

        # run the summarization using the method
        if self.method == 1:
            try:
                result = textRank(text, param[0]) # result is a list of top sentences!!
            except:
                print("Error")
                result = []
        elif self.method == 2:
            try:
                result = k_means(text, param[0]) # add param for number of clusters?
            except:
                result = []
        elif self.method == 3:
            #result = bert(text)
            model = Summarizer()
            print(text)
            result = bertSum(text, model)
        elif self.method == 4:
            result = bart(text)
            print(result)
        elif self.method == 5:
            result = llm_summarizer(text)
        else:
            raise ValueError(f"Unsupported summarization method: {self.method}")
        print("result: ",result)

        return result 
