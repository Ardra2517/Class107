import pandas as pd
import plotly.graph_objects as pgo
import csv

file=pd.read_csv("data3a.csv")
student=file.loc[file['student_id']=="TRL_rst"]
print(student.groupby("level")["attempt"].mean())


fig=pgo.Figure(pgo.Bar(
    x=student.groupby("level")["attempt"].mean(),
    y=["Level 1","Level 2","Level 3","Level 4"],
    orientation='h'
))

fig.show()