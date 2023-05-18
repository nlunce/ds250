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
# Load dataset
df = pd.read_json("flights_missing.json")

df.columns

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
# Filter out -999 values from delay_late_aircraft
filter_df["num_of_delays_late_aircraft"] = filter_df[
    "num_of_delays_late_aircraft"
].replace({-999: np.nan})
filter_df

# %%
# Calculate average 'num_of_delays_late_aircraft'
avg_delays_late_aircraft = filter_df["num_of_delays_late_aircraft"].mean().round()

print(f"The average number of delays late aircrafts is {avg_delays_late_aircraft}")

# %%
# Replace Nan values with avg_delays_late_aircraft
filter_df["num_of_delays_late_aircraft"] = filter_df[
    "num_of_delays_late_aircraft"
].replace({np.nan: avg_delays_late_aircraft})

filter_df

# %%
# Drop n/a months
filter_df = filter_df.query('month != "n/a"')

filter_df

# %%
# Calculate true total delays because of weather. ***JUST FOR VERIFICATION***
total_flights_delayed_by_weather = 0

total_weather = filter_df["num_of_delays_weather"].sum()
total_flights_delayed_by_weather += total_weather

total_delays_late_aircraft = filter_df["num_of_delays_late_aircraft"].sum() * 0.3

total_flights_delayed_by_weather += total_delays_late_aircraft

total_flights_delayed_by_weather

fourty_months = ["April", "May", "June", "July", "August"]
sixty_five_months = [
    "January",
    "Febuary",
    "March",
    "September",
    "October",
    "November",
    "December",
]

sixty_five_table_b = filter_df["month"].isin(sixty_five_months)

fourty_table_b = filter_df["month"].isin(fourty_months)
fourty_table = filter_df[fourty_table_b]

sixty_five_table = filter_df[sixty_five_table_b]

total_nas_weather = fourty_table["num_of_delays_nas"].sum() * 0.4

total_nas_weather += sixty_five_table["num_of_delays_nas"].sum() * 0.65

total_flights_delayed_by_weather += total_nas_weather

total_flights_delayed_by_weather

# %%
# Add 'true_num_of_delays_weather'
filter_df["true_num_of_delays_weather"] = 0
filter_df

# %%
# Define the conditions
condition1 = filter_df["month"].isin(["April", "May", "June", "July", "August"])
condition2 = ~filter_df["month"].isin(["April", "May", "June", "July", "August"])

# Calculate the values for the new column based on the conditions
filter_df.loc[condition1, "true_num_of_delays_weather"] = (
    filter_df["num_of_delays_weather"]
    + (filter_df["num_of_delays_late_aircraft"] * 0.30)
    + (filter_df["num_of_delays_nas"] * 0.40)
).round()

filter_df.loc[condition2, "true_num_of_delays_weather"] = (
    filter_df["num_of_delays_weather"]
    + (filter_df["num_of_delays_late_aircraft"] * 0.30)
    + (df["num_of_delays_nas"] * 0.65)
).round()


filter_df

# %%
# Final table

final = filter_df.rename(
    columns={"num_of_delays_weather": "num_of_delays_severe_weather"}
)
final = final.rename(columns={"true_num_of_delays_weather": "total_num_delays_weather"})
final = final.filter(
    [
        "month",
        "num_of_delays_late_aircraft",
        "num_of_delays_nas",
        "num_of_delays_severe_weather",
        "total_num_delays_weather",
    ]
)
final
