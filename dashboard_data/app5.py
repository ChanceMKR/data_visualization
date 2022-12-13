# -*- coding: utf-8 -*-

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from pathlib import Path
import pandas as pd
import numpy as np
import plotly.express as px

script_dir = Path(__file__).parent.absolute()
data = pd.read_csv(str(script_dir) + "/explife.csv")
app = dash.Dash()


app.layout = html.Div([
    html.H6("GDP per capita vs Life Expectancy"),
    html.Div(style = {"width" : "90%", "padding-left" : "5%", "padding-right" : "5%"}, children = [
            dcc.Slider(
                min = data["year"].min(),
                max = data["year"].max(),
                step = None,
                value = data["year"].min(),
                marks = {int(year) : str(year) for year in data["year"].unique()},
                id = "year-slider")
        ]),
    html.Div(children = [
        dcc.RadioItems(
            options = [{"label" : "Raw", "value" : "raw"},
                       {"label" : "Log", "value" : "log"}],
            value = "raw",
            labelStyle = {"display" : "block"},
            id = "xaxis-transformation"
            )
        ]),
    html.Br(),
    dcc.Graph(id = "my-output"),
])


@app.callback(
    Output(component_id = "my-output", component_property = "figure"),
    Input(component_id = "year-slider", component_property = "value"),
    Input(component_id = "xaxis-transformation", component_property = "value")
)
def plotting_figure(year, trans_type):
    tdat = data.loc[data.year == year, :].copy()
    if trans_type == "log":
        tdat.gdpPercap = np.log(tdat.gdpPercap)
        
    fig = px.scatter(data_frame = tdat,
                     x = "gdpPercap", 
                     y = "lifeExp",
                     size = "pop",
                     color = "continent",
                     hover_name = "country",
                     size_max = 60)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

