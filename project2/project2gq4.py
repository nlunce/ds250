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

# %%
# Finalize
final = filter_df.rename(
    columns={"num_of_delays_weather": "num_of_delays_severe_weather"}
).filter(
    [
        "airport_code",
        "month",
        "num_of_delays_nas",
        "num_of_delays_late_aircraft",
        "num_of_delays_severe_weather",
        "total_num_weather_delays",
        "num_of_delays_total",
    ]
)

final

# %%

final = final.groupby("airport_code", as_index=False).agg(
    total_weather_delays=("total_num_weather_delays", "sum"),
    total_delays=("num_of_delays_total", "sum"),
)

final["total_weather_delays"] = final["total_weather_delays"].astype(int)

final["Percent of Total Delays Caused by Weather"] = (
    final["total_weather_delays"] / final["total_delays"]
).apply(lambda x: f"{x:0.2f}" + "%")


final = final.rename(
    columns={
        "total_weather_delays": "Weather Delays",
        "total_delays": "Total Delays",
        "airport_code": "Airport Code",
    }
)

final


# %%
graph1 = (
    alt.Chart(final, title="Total Number of Delays")
    .mark_bar()
    .encode(
        x=alt.X("Airport Code:O", axis=alt.Axis(title="Airport")),
        y=alt.Y("Total Delays:Q", axis=alt.Axis(title="Delays")),
    )
)


graph2 = (
    alt.Chart(final, title="Total Delays Caused by Weather")
    .mark_bar(color="#900dd6")
    .encode(
        x=alt.X("Airport Code:O", axis=alt.Axis(title="Airport")),
        y=alt.Y("Weather Delays:Q", axis=alt.Axis(title="Delays")),
    )
)


graph2
# %%

graph3 = graph1 + graph2

graph3 = graph3.properties(
    title="Total Number of Delays Compared to Delays Caused by Weather"
)
final_graph = graph3 | graph1 | graph2
final_graph
