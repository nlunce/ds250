#%%
# Importing
import pandas as pd
import altair as alt
import numpy as np

from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate

#%%
pd.set_option('display.max_columns', 200)
df = pd.read_json('flights_missing.json')
df
#%%
s = pd.DataFrame(np.random.randint(0, 10, size=(7, 4)), columns=['A', 'B', 'C', 'D'])
s
#%%
# isin()

in_out = s['A'].isin([2,4,6])
in_out

#%%
# s.where() function

s.A.where(s.A > 5, 0)
# puts 0 instead of NaN

s.A = s.A.where(s.A > 5, 9999)
# s['A'] = s['A'].where(s.A > 5, 9999) #same thing ^^
# Changes the dataframe

s

#%%
s['A'][s['A'] < 5] = -1
s
# make changes to just one row


#%%
# numpy where function

np.where(s > 5, s, -s)

#%%
# replace 

s.replace(5, 99)
s.replace(5, 99, inplace=True)
# this changes the data frame ^^ `inplace=true`

s['B'].replace(8, 99)
# just one row

lookup = {
    5: 99,
    7: -1,
    8: 4
}

s.replace(lookup)
# dictionary replace 

s.dtypes
# shows datatypes of columns

s.replace([1,2,3], 99)
# works too