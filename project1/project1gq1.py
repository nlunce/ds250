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
# Query Nathan
nathan = names.query('name == "Nathan"')
nathan

#%%
# Birth year of nathan dataframe
birthYearDf= pd.DataFrame({'Year': [2002]})
birthYearDf
birthYearLine = alt.Chart(birthYearDf).mark_rule(color="red").encode(x = "Year")
birthYearLine

#%%
# Add label
birthYearLabel = alt.Chart(birthYearDf).mark_text(
    text='Birth of Nathan Lunceford (2002)',
    align='left',
    baseline='middle',
    dx=10,
    dy=250
).encode(
    x='year',
    y=alt.value(0)  # adjust label position
)

#%%
# Chart Nathan
chartNathan = (alt.Chart(nathan, title = 'Name of Nathan over the years')
  .encode(
    x = alt.X('year', axis = alt.Axis(format= 'd', title= 'Year')),
    y = alt.Y('Total', axis= alt.Axis(format= 'd', 
                title='Children with the name Nathan', ))
    )
  .mark_line()
)

chartNathan



#%%
# Chart Nathan + birth year DF + Label
chart = chartNathan + birthYearLine + birthYearLabel
chart





