#%%
# Importing
import pandas as pd
import altair as alt
import numpy as np

from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate

#%%
pd.set_option('display.max_columns', 200)
df = pd.read_json('flights_missing.json')
df