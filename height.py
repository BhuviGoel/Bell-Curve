import plotly.figure_factory as ff
import pandas as pd
import csv

data = pd.read_csv(r"C:\Users\bhuvi\Google Drive\Code\Python\Class 108 - Bell Curve\data.csv")

fig = ff.create_distplot([data["Height(Inches)"].tolist()], ["Height"], show_hist=False)
fig.show()