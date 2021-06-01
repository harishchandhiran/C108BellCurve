import scipy
import pandas as pd
import csv
import plotly.figure_factory as pff

data = pd.read_csv("data.csv")
fig = pff.create_distplot([data["Avg Rating"].tolist()], ["Avg Rating"])
fig.show()