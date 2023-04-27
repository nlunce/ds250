#%%
# Importing
import pandas as pd
import altair as alt
import numpy as np

from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate

#%%
# Load dataset
names = pd.read_csv('names_year.csv')
names

#%%
names.columns()
#%%
# Charts

nathan = names.query('name == "Nathan"')
nathan

david = names.query('name == "David"')
david
#%%
# Chart Nathan

line_df = pd.DataFrame({'year': [2002]})
line_df
line = alt.Chart(line_df).mark_rule(color="red").encode(x = "year")
line

#%%

chartNathan = (alt.Chart(nathan, title = 'Name of Nathan over the years')
  .encode(
    x = alt.X('year', axis = alt.Axis(format= 'd', title= 'Year')),
    y = alt.Y('Total', axis= alt.Axis(format= 'd', 
                title='Children with name Nathan', ))
    )
  .mark_line()
)

chartNathan

chartNathanWithBirth = chartNathan + line
chartNathanWithBirth

#%%
#Chart David

chartDavid = (alt.Chart(david, title = 'Name of David over the years')
  .encode(
    alt.X('year'),
    alt.Y('Total')
    )
  .mark_line()
)
chartDavid

#%%

chart = chartNathan + chartDavid
chart

