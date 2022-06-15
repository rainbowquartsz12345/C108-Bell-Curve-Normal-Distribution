import pandas as pd
import plotly.figure_factory as pf

df = pd.read_csv("data.csv")
x = df["Height(Inches)"].tolist()

fig = pf.create_distplot([df["Height(Inches)"].tolist()] , ["height data"] , show_hist = False )
fig.show()

