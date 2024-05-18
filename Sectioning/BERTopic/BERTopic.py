import os, sys
import argparse
import ast

from collections import Counter
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from transformers import AutoTokenizer, AutoModelForTokenClassification

import advertools as adv
from bertopic import BERTopic





if __name__ == '__main__':
    # Load sectioned data
    data = pd.read_csv('sectioned_data_2022.csv')
