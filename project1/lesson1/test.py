#%%
import pandas as pd
import altair as alt

# Load dataset
names = pd.read_csv('names_year.csv')

# Query Nathan
nathan = names.query('name == "Nathan"')

# Birth year of Nathan dataframe
birthYearDf = pd.DataFrame({'year': [2002]})

# Create birth year line chart
birthYearLine = alt.Chart(birthYearDf).mark_rule(color="red").encode(x="year")

# Create Nathan chart
chartNathan = (alt.Chart(nathan, title='Name of Nathan over the years')
               .encode(
                   x=alt.X('year', axis=alt.Axis(format='d', title='Year')),
                   y=alt.Y('Total', axis=alt.Axis(format='d', title='Children with the name Nathan'))
               )
               .mark_line()
              )

# Add label to birth year line
label = alt.Chart(birthYearDf).mark_text(
    text='birth of Nathan',
    align='left',
    baseline='middle',
    dx=10
).encode(
    x='year',
    y=alt.value(0)  # adjust label position
)

# Combine charts and label
chart = (chartNathan + birthYearLine + label)

# Show chart
chart