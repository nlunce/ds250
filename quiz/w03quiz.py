#%%
# Importing
import pandas as pd
import altair as alt
import numpy as np

from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate

#%%
# Load Dataset
data = pd.read_csv('names_year.csv')
data

#%%
# Question 1
# How many babies are named “Oliver” in the state of Utah for all years?
# 116586



# Load data

# Filter data for name "Oliver" and state "Utah"
oliver = data.query('name == "Oliver"')

oliver_total_ut = oliver['UT'].sum()


print(oliver_total_ut)

#%%
# Question 1
# What was the earliest year that the name “Felisha” was used?
#1964
felisha = data.query('name == "Felisha"')
felisha_sorted = felisha.sort_values('year')
felisha_sorted


# earliest_year = felisha_sorted.iloc[0]['year']

# print(earliest_year)



