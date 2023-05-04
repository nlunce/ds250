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
# Filter data for desired name
bruce = data.query('name == "Bruce"')
bruce

# bruce = data[data['name'] == "Bruce"]
# bruce

#%%
# Create Bruce charts
bruceChart = (alt.Chart(bruce, title='Name of Bruce over the years')
         .encode(x=alt.X('year', axis=alt.Axis(format='d', title='Year')),
                 y=alt.Y('Total', axis=alt.Axis(format='d', title='Children with the name Bruce')),
                 )
         .mark_line())

bruceChart
# %%
# Create an lable dataframe for when the first Batman movie came out
batman1943Df= pd.DataFrame({'year': [1943]})
batman1943Df
batman1943Line = alt.Chart(batman1943Df).mark_rule(color="red").encode(x = "year")
batman1943Line

batman1943LineLabel = alt.Chart(batman1943Df).mark_text(
    text='First Batman movie comes out (1943)',
    align='left',
    baseline='middle',
    dx=10,
    dy=10,
    color='red').encode(
    x='year',
    y=alt.value(0)  # adjust label position
)

batman1943LineLabel



#%%
# Final chart
chart = bruceChart + batman1943Line + batman1943LineLabel
chart

