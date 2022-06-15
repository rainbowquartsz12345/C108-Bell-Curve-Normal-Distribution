import pandas as pd
import plotly.figure_factory as pf

df = pd.read_csv("rating.csv")
x = df["Avg Rating"].tolist()

fig = pf.create_distplot( [df["Avg Rating"].tolist()], ["average ratings"], show_hist = False)
fig.show()