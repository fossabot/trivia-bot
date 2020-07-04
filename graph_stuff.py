import plotly.graph_objects as go
import numpy as np

Running = True

list = []

while Running:
    ainput = input()
    if ainput != 'x':
        try:
            int(ainput)
            list += str(ainput)
        except:
            print('a')
    else:
        print('a')
        Running = False

y = list
x = np.arange(len(y))

print(str(x))
print(str(y))

fig = go.Figure(data=go.Scatter(x=x, y=y))

fig.show()
