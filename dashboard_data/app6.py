# -*- coding: utf-8 -*-

import dash
from dash import dash_table as dt
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
    html.Div([
        html.H6("Top 10 country for life expectancy"),
        html.Div(style = {"width" : "80%", "padding-left" : "10%", "padding-right" : "10%"}, children = [
                dcc.Slider(
                    min = data["year"].min(),
                    max = data["year"].max(),
                    step = None,
                    value = data["year"].min(),
                    marks = {int(year) : str(year) for year in data["year"].unique()},
                    id = "year-slider1")
            ]),
        html.Div(style = {"margin-top" : "30px", "width" : "50%"}, children = [
                "Maximum number of rows: ",
                dcc.Input(id = "my-input", value = 10, type = "number", style = {"width" : "5%"})
            ]),
        dt.DataTable(id = "table-content")
        ],
        style = {"width" : "49%", "display" : "inline-block"}),
    html.Div([
    html.H6("GDP per capita vs Life Expectancy"),
    html.Div(style = {"width" : "80%", "padding-left" : "10%", "padding-right" : "10%"}, children = [
            dcc.Slider(
                min = data["year"].min(),
                max = data["year"].max(),
                step = None,
                value = data["year"].min(),
                marks = {int(year) : str(year) for year in data["year"].unique()},
                id = "year-slider2")
        ]),
    html.Div(style = {"margin-top" : "30px"}, children = [
        dcc.RadioItems(
            options = [{"label" : "Raw", "value" : "raw"},
                       {"label" : "Log", "value" : "log"}],
            value = "raw",
            labelStyle = {"display" : "block"},
            id = "xaxis-transformation"
            )
        ]),
    html.Br(),
    dcc.Graph(id = "my-output")
    ], style = {"width" : "49%", "display" : "inline-block"})
])


@app.callback(
    Output(component_id = "my-output", component_property = "figure"),
    Input(component_id = "year-slider2", component_property = "value"),
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

@app.callback(
    Output(component_id = "table-content", component_property = "data"),
    Output(component_id = "table-content", component_property = "columns"),
    Input(component_id = "year-slider1", component_property = "value"),
    Input(component_id = "my-input", component_property = "value")
)
def generate_table(year, max_rows = 10):
    tdata = data.loc[data.year == year, :].copy()
    tdata = tdata.sort_values("lifeExp", ascending = False).iloc[:max_rows, :]
    return tdata.to_dict('records'), [{"name": i, "id": i} for i in tdata.columns]
                 


if __name__ == '__main__':
    app.run_server(debug=True)
