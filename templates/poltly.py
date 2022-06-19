
import plotly.express as px
import pandas as pd
import plotly

df = pd.read_json("data.json")

values = df["Kategorie"]

fig = px.pie(df,
             values=values,
             names=names,
             title="KUCHENDIAGRAMM")

fig.update_traces(
    textposition = 'inside',
    textinfo='percent+label'
    )

fig.update


