# -*- coding: utf-8 -*-

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
# import pandas as pd
# import plotly.express as px
# import plotly.io as pio
# import os
# import numpy as np


app = dash.Dash()

app.layout = html.Div([
    html.H6("Self-introduction"),
    html.Div([
        "Input: ",
        dcc.Input(id = "my-input", value = "name", type = "text")
    ]),
    html.Br(),
    html.Div(id = "my-output"),
])


@app.callback(
    Output(component_id = "my-output", component_property = "children"),
    Input(component_id = "my-input", component_property = "value")
)
def update_output(name):
    return 'My name is {name}'.format(name = name)


if __name__ == '__main__':
    app.run_server(debug=True)