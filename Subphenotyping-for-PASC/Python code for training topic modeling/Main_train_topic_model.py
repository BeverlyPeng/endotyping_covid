"""
===========================================
Train topic model
===========================================

"""

# Author: Hao Zhang
# License: Apache License Version 2.0


import numpy as np
import pandas as pd
import scipy.io as sio
from scipy.sparse import coo_matrix
from pydpm.model import PFA
import re

import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

import sklearn.cluster
from sklearn import preprocessing
import umap
from collections import Counter
from sklearn.metrics import silhouette_score 

#### UCSF
# data = pd.read_csv('../../preprocessed_n669_to1.csv') # (669, 32)
# data = data[['abdom', 'back', 'balan', 'chest', 'chills', 'concen', 'const', 'cough', 'cramps', 'diarr', 'dizz', 'faint', 'fatig', 'fever', 'head', 'heartrace', 'loss', 'muscle', 'nausea', 'numb', 'odor', 'pain', 'painsex', 'rash', 'runny', 'short', 'sleep', 'smell', 'sore', 'temp', 'vision', 'vomit']]
# N = 669

#### ISMSS
# data = pd.read_csv('../../UCSF_8_21_2024_DATAEXPORT_original_survey.csv') # (628, 49)
# N = 615
# data = data[list(filter(re.compile("currentsymptoms_.*").match, data.columns))]
# del data["currentsymptoms_45"]
# del data["currentsymptoms_46"]

#### ISMSS+Emory
# data = pd.read_csv('../../emory_and_sinai_n675.csv') # (675, 41)
# N = 675

#### Cardiff
data = pd.read_csv("../../cardiff_data_all_n318.csv") # (318, 36)
N = 318
data = data.iloc[:, 2:]

X = np.array(data.T, order='C')

# seeds = [0, 2147483648, 791027963, 3345801497, 1226153587, 3566202621, 327879993, 3442034491, 170988731, 1851704852, 2088539408]

for v in range(1, 11): 
    for K in range(2, 82): 
        print("v, k:", v, K)
        # seed = seeds[v]
        # print("SEED  :", seed, np.random.get_state()[1][0])
        trained_topic_model_folder = f"../trained_topic_model_cardiff_n318_v{v}/"
        outputfilename = f'PFA_trained_model_n{N}_k{K}.mat'
        model=PFA(K, 'cpu')
        model.initial(X)
        # model.initial(X, seed)
        model.train(iter_all=1000, burn_in = 500, output_folder = trained_topic_model_folder, outputfilename = outputfilename)
        print(v, K)
