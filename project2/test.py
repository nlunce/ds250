#%%
import pandas as pd
import altair as alt
import calendar

#%%

# Read the JSON file into a DataFrame
df = pd.read_json('flights_missing.json')

# Filter the DataFrame and select relevant columns
filter_df = df.filter(['month', 'num_of_flights_total', 'num_of_delays_late_aircraft', 'minutes_delayed_total', 'num_of_delays_total'])

# Remove rows with negative values for 'num_of_delays_late_aircraft'
filter_df = filter_df[filter_df['num_of_delays_late_aircraft'] > 0]

# Remove rows with 'month' value equal to 'n/a'
filter_df = filter_df[filter_df['month'] != 'n/a']

# Convert 'month' column to categorical data type with ordered months
month_order = list(calendar.month_name[1:])
filter_df['month'] = pd.Categorical(filter_df['month'], categories=month_order, ordered=True)

# Group by month and calculate the average number of delays
chart = filter_df.groupby('month')['num_of_delays_total'].mean().reset_index()

# Create the chart using Altair
final = alt.Chart(chart).mark_bar().encode(
    x=alt.X('month:O', sort=month_order, title='Month'),
    y=alt.Y('num_of_delays_total:Q', title='Average Number of Delays')
).properties(
    title='Average Number of Delays by Month'
).configure_axisX(
    labelAngle=45
)

final
