#%%
import pandas as pd
import altair as alt
import numpy as np

from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate

#%%
# Load data
data = pd.read_csv('names_year.csv')
data

#%%
# Filter data for desired names
names = ['Mary', 'Martha', 'Peter', 'Paul']
filtered_data = data[data['name'].isin(names) & (data['year'] >= 1920) & (data['year'] <= 2000)]
filtered_data

#%%
# Create final chart
chart = (alt.Chart(filtered_data, title='Names over the years')
         .encode(x=alt.X('year', axis=alt.Axis(format='d', title='Year')),
                 y=alt.Y('Total', axis=alt.Axis(format='d', title='Children with the name')),
                 color=alt.Color('name', title='Name'))
         .mark_line())

chart
# %%
