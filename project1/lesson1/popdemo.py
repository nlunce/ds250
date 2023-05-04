# Importing
#%%
import pandas as pd
import altair as alt
import numpy as np
from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate


#%%
# Importing
pop = pd.read_csv('population-and-demography.csv')
pop


#%%
yearCount = pop.filter(['Country name', 'Year', 'Population'])
yearCount


#%%
# Question: Display years between 1980 to 200 and the countries of USA or Candada

qstr = """ 
Year >= 1980 & Year <= 2000 & \
(`Country name` == 'United States' | \
`Country name` == 'Canada')
"""
tf = yearCount.query(qstr)
tf
# %%

date = pd.DataFrame({'Year': [1999]})
date

line =(
alt.Chart(date)
.encode(alt.X('Year'))
.mark_rule(color='red')
)

line

# %%
