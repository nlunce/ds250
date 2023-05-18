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
    "month",
    "num_of_delays_nas",
    "num_of_delays_weather",
    "num_of_delays_late_aircraft",
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

filter_df

# %%
# mild nas
filter_df = filter_df.assign(
    num_delays_mild_weather_nas=np.where(
        condition,
        filter_df["num_of_delays_nas"] * 0.40,
        filter_df["num_of_delays_nas"] * 0.65,
    )
)

filter_df

# %%
# weather total and sever

filter_df = filter_df.assign(
    total_num_weather_delays=(
        filter_df["num_of_delays_weather"]
        + filter_df["num_delays_mild_weather_late_aircraft"]
        + filter_df["num_delays_mild_weather_nas"]
    ).round()
)

# %%
# Finalize
final = filter_df.rename(
    columns={"num_of_delays_weather": "num_of_delays_severe_weather"}
).filter(
    [
        "month",
        "num_of_delays_nas",
        "num_of_delays_late_aircraft",
        "num_of_delays_severe_weather",
        "total_num_weather_delays",
    ]
)


final
