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

df["num_of_delays_late_aircraft"] = df["num_of_delays_late_aircraft"].replace(
    {-999: np.nan}
)

df["minutes_delayed_nas"] = df["minutes_delayed_nas"].replace({-999: np.nan})

df["month"] = df["month"].replace({"n/a": np.nan})


df["airport_name"] = df["airport_name"].replace({"": np.nan})

df.describe()


# %%
df2 = df["num_of_delays_carrier"] == "1500+"
df2

df[df2]

# %%
df.to_json("clean_flights_missing.json")

# %%
df2 = pd.read_json("clean_flights_missing.json")
df2

# %%
json = df2.head(1)
json.to_json()
