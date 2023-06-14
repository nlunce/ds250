# %%
# Importing
import pandas as pd
import altair as alt
import numpy as np

from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

# %%
# Load dataset
dwell = pd.read_csv("dwellings_ml.csv")

dwell.columns

# %%
# Crosstab
# facet columns =before 1980

