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
# Query Brittany
brittany = names.query('name == "Brittany"')
brittany

#%%
# Chart Brittany
chartBritrany = (alt.Chart(brittany, title = 'Name of Brittany over the years')
  .encode(
    x = alt.X('year', axis = alt.Axis(format= 'd', title= 'Year')),
    y = alt.Y('Total', axis= alt.Axis(format= 'd', 
                title='Children with the name Brittany' ))
    )
  .mark_line()
)

chartBritrany

#%%
# Peak Brittany year Dataframe
year1990Df = pd.DataFrame({'Year': [1990]})
year1990Df
year1990Line = alt.Chart(year1990Df).mark_rule(color="red").encode(x = "Year")
year1990Line

#%%
# Year 1990 Label
year1990LineLable = alt.Chart(year1990Df).mark_text(
    text='Year where most Brittanys were born (1990)',
    align='left',
    baseline='middle',
    dx=10,
    dy=10,
    color= 'red'
).encode(
    x='Year',
    y=alt.value(50)  # adjust label position
)

#%%
# Final Chart
chart = chartBritrany + year1990Line + year1990LineLable
chart

#%%
# Table showing what year has most Brittanys
filBrittany = brittany.filter(['name', 'year', 'Total'])
filBrittany


table = filBrittany.query('year >= 1985 & year <= 1995')
table
# maxBrittany = filBrittany.max()
# maxBrittany 



# %%
