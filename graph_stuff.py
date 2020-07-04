import plotly.graph_objects as go
import numpy as np

Running = True

list = []

while Running:
    ainput = input()
    ainput = ainput.split()[-1]
    if ainput != "x":
        try:
            int(ainput)
            list.append(str(ainput))
        except:
            print("a")
    else:
        print("a")
        Running = False

y = list
x = np.arange(len(y))

print(str(x))
print(str(y))

fig = go.Figure(data=go.Scatter(x=x, y=y))

fig.update_layout(
    title="Trivia Bot Server Count",
    xaxis_title="Time",
    yaxis_title="Number of Servers",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    annotations=[
        go.layout.Annotation(
            showarrow=False,
            text="Graphing Software (c) 2020 gubareve",
            xanchor="right",
            x=1,
            yanchor="top",
            y=0.05,
        )
    ],
)

fig.show()
