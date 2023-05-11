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
# Filter data
filter_df = df.filter(['airport_code', 'num_of_flights_total', 'num_of_delays_late_aircraft', 'minutes_delayed_total' ])

#%%
# Remove rows with negative values
filter_df = filter_df.query('num_of_delays_late_aircraft > 0')

#%%
# Group by airport code
group = filter_df.groupby('airport_code').agg('sum')

#%%
# Add and calculate delay rate percentage and average_delay_hours columns
group['delay_rate_percent'] = (group['num_of_delays_late_aircraft']/group['num_of_flights_total'])*100

group['average_delay_hours'] = (group['minutes_delayed_total']/group['num_of_delays_late_aircraft'])/60
 
#%%
# Drop minutes_delayed_total column

final = group.drop('minutes_delayed_total', axis=1)
final
