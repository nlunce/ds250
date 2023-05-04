#%%
import pandas as pd
import altair as alt
import numpy as np

from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate

#%%
# Load data
data = pd.read_csv('pokemon_data.csv')
data

#%%
# Read Headers
data.columns

#%%
# Read each Column
data['Name'][0:5]
# This also works
# data.Name 
data[['Name', 'HP']][0:5]

#%%
# Read each Row
data.iloc[1]
# iloc stands for integer location
data.loc[data['Type 1'] == 'Fire']
#%%
# Read a specific location (R,C)
data.iloc[2,1]
