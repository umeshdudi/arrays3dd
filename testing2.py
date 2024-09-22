from first import normalize_array
import numpy as np 
import plotly.graph_objects as go

b,d = normalize_array()
x,y = np.arange(b.shape[0]), np.arange(b.shape[1])
X,Y = np.meshgrid(x,y)
fig = go.Figure()

fig.add_trace(go.Surface(
    z = b,
    x = X,
    y = Y,
    name = 'original array',
    colorscale = 'sunset'
))
fig.add_trace(go.Surface(
    z = d,
    x = X,
    y = Y,
    name = 'normalize array',
    colorscale = 'Viridis'
))

fig.update_layout(
    title = 'arrays',
    scene = dict(
        xaxis_title ='X',
        yaxis_title = 'Y',
        zaxis_title = 'Value',
        zaxis = dict(
            range = [
                np.min(b), np.max(b),
            ]
        )
    ),
    updatemenus = [
        dict(
            type = 'dropdown',
            x = 1.05,
            y = 0.8,
            buttons = [
                dict(label='original',method = 'update', args = [{'visible':[True, False]}]),
                dict(label = 'normalized', method = 'update', args = [{'visible': [False, True]}]),
                dict(label = 'both', method = 'update', args = [{'visible': [True, True]}])
            ]
        )
    ]
)

fig.show()