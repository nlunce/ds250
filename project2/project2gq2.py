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
# Filter Data
filter_df = df.filter(["month", "num_of_delays_total"])

filter_df = filter_df.query('month != "n/a"')

month_order = [
    "January",
    "Febuary",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

filter_df["month"] = pd.Categorical(
    filter_df["month"], categories=month_order, ordered=True
)


# %%
# Group data
chart = filter_df.groupby("month", as_index=False).agg("mean")
chart["average_num_of_delays"] = chart["num_of_delays_total"]
chart = chart.drop(["num_of_delays_total"], axis=1)
chart


# %%
# Graph data
graph = (
    alt.Chart(chart, title="Average Number of Delays by Month")
    .mark_bar()
    .encode(
        x=alt.X("month:O", axis=alt.Axis(title="Month"), sort=month_order),
        y=alt.Y(
            "average_num_of_delays:Q", axis=alt.Axis(title="Average Number of Delays")
        ),
    )
    .configure_axis(labelFontSize=20, titleFontSize=30)
    .configure_title(fontSize=35)
    .properties(width=800, height=400)
)
graph
