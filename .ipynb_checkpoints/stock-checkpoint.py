import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
#import seaborn as sns

df = pd.read_csv('archive/sp500_companies.csv')
a=df.head()
print(a)
print(df.isnull().sum())