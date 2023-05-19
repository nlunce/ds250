# %%
import pandas as pd
import altair as alt
import numpy as np

from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate

# %%

mpg = pd.read_csv("mpg.csv")

chart = alt.Chart(mpg).encode(x="displ", y="hwy").mark_circle()

chart

# print(
#     mpg.head(5)
#     .filter(["manufacturer", "model", "year", "hwy"])
#     .to_markdown(index=False)
# )

# %%
