import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import asyncio
import joblib
import sys

np.random.seed(0)

# Первый узел DAG
async def load_dataset():
    df_penguins = sns.load_dataset(sys.argv[1])
    return df_penguins

async def sample_get(df, n=150):
    return df.sample(n)

df = asyncio.run(sample_get(asyncio.run(load_dataset())))
joblib.dump(df, sys.argv[2])