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
df = pd.read_json('flights_missing.json')
df

#%%
filter_df = df.filter(['airport_code','month', 'num_of_flights_total', 'num_of_delays_late_aircraft', 'minutes_delayed_total' ])

#%%
# Remove rows with negative values
filter_df = filter_df.query('num_of_delays_late_aircraft > 0')

#%%
# Group by airport code
group = filter_df.groupby('month')

group.first()