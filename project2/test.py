# %%
# Importing
import pandas as pd
import altair as alt
import numpy as np

from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate

# %%
# Load dataset
df = pd.read_json("flights_missing.json")
# %%
# Filter Data Columns
desired_columns = [
    "airport_code",
    "month",
    "num_of_delays_nas",
    "num_of_delays_weather",
    "num_of_delays_late_aircraft",
    "num_of_delays_total",
]
filter_df = df.filter(desired_columns)


# %%
# Filter data
filter_df["num_of_delays_late_aircraft"] = filter_df[
    "num_of_delays_late_aircraft"
].replace({-999: np.nan})

# Calculate average 'num_of_delays_late_aircraft'
avg_delays_late_aircraft = filter_df["num_of_delays_late_aircraft"].mean().round()

# Replace Nan values with avg_delays_late_aircraft
filter_df["num_of_delays_late_aircraft"] = filter_df[
    "num_of_delays_late_aircraft"
].replace({np.nan: avg_delays_late_aircraft})

# Drop n/a months
filter_df = filter_df.query('month != "n/a"')


# %%
# Define the conditions
months = ["April", "May", "June", "July", "August"]
condition = filter_df["month"].isin(months)


# %%
# Mild late
filter_df = filter_df.assign(
    num_delays_mild_weather_late_aircraft=filter_df["num_of_delays_late_aircraft"]
    * 0.30
)


# %%
# mild nas
filter_df = filter_df.assign(
    num_delays_mild_weather_nas=np.where(
        condition,
        filter_df["num_of_delays_nas"] * 0.40,
        filter_df["num_of_delays_nas"] * 0.65,
    )
)

# %%
# weather total and sever

filter_df = filter_df.assign(
    total_num_weather_delays=(
        filter_df["num_of_delays_weather"]
        + filter_df["num_delays_mild_weather_late_aircraft"]
        + filter_df["num_delays_mild_weather_nas"]
    ).round()
)

filter_df


# %%
graph2 = (
    alt.Chart(
        filter_df, title="Total Number of Delays Compared to Delays Caused by Weather"
    )
    .mark_bar(color="#900dd6")
    .encode(
        x=alt.X("airport_code:O", axis=alt.Axis(title="Airport")),
        y=alt.Y("total_num_weather_delays:Q", axis=alt.Axis(title="Delays")),
        color=alt.Color(
            "num_delays_mild_weather_nas:N",
        ),
    )
)

graph2

# %%
'{"airport_code":{"0":"ATL"},
 "airport_name":{"0":"Atlanta, GA: Hartsfield-Jackson Atlanta International"},
 "month":{"0":"January"},
 "year":{"0":2005.0},
 "num_of_flights_total":{"0":35048},
 "num_of_delays_carrier":{"0":"1500+"},
 "num_of_delays_late_aircraft":{"0":null},
 "num_of_delays_nas":{"0":4598},
 "num_of_delays_security":{"0":10},
 "num_of_delays_weather":{"0":448},
 "num_of_delays_total":{"0":8355},
 "minutes_delayed_carrier":{"0":116423.0},
 "minutes_delayed_late_aircraft":{"0":104415},
 "minutes_delayed_nas":{"0":207467.0},
 "minutes_delayed_security":{"0":297},
 "minutes_delayed_weather":{"0":36931},
 "minutes_delayed_total":{"0":465533}}'
