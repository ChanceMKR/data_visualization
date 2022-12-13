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
    html.Div(style = {"width" : "80%", "padding-left" : "10%", "padding-right" : "10%"}, children = [
            dcc.Slider(
                min = data["year"].min(),
                max = data["year"].max(),
                step = None,
                value = data["year"].min(),
                marks = {int(year) : str(year) for year in data["year"].unique()},
                id = "year-slider")
        ]),
    html.Br(),
    html.Div(children = [
        html.H5("Top 10 country for life expectancy"),
        html.Br(),
        html.Div(style = {"margin-top" : "30px", "width" : "50%"}, children = [
                "Maximum number of rows: ",
                dcc.Input(id = "max-rows", value = 10, type = "number", style = {"width" : "5%"})
            ]),
        html.Div(children = [dt.DataTable(id = "table-content")])
        ],
        style = {"width" : "49%", "display" : "inline-block", "vertical-align" : "top"}),
    html.Div([
    html.H5("GDP per capita vs Life Expectancy"),
    html.Br(),
    html.Div(children = [
        dcc.RadioItems(
            options = [{"label" : "Raw", "value" : "raw"},
                       {"label" : "Log", "value" : "log"}],
            value = "raw",
            labelStyle = {"display" : "inline"},
            id = "xaxis-transformation"
            )
        ]),
    dcc.Graph(id = "my-output")
    ], style = {"width" : "49%", "display" : "inline-block", "vertical-align" : "top"})
])


@app.callback(
    Output(component_id = "my-output", component_property = "figure"),
    Output(component_id = "table-content", component_property = "data"),
    Output(component_id = "table-content", component_property = "columns"),
    Input(component_id = "year-slider", component_property = "value"),
    Input(component_id = "xaxis-transformation", component_property = "value"),
    Input(component_id = "max-rows", component_property = "value")
)
def update_content(year, trans_type, max_rows = 10):
    fig = plotting_figure(year, trans_type)
    table = generate_table(year, max_rows)
    return fig, table[0], table[1]


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
    
    fig.update_layout(plot_bgcolor = "#FFFFFF", margin = dict(t = 10))
    fig.update_xaxes(showline = True, showgrid = True, zeroline = True, zerolinewidth = 1,
                     linecolor = "black", gridcolor = "grey", zerolinecolor = "grey")
    fig.update_yaxes(showline = True, showgrid = True, zeroline = True, zerolinewidth = 1,
                     linecolor = "black", gridcolor = "grey", zerolinecolor = "grey")
    
    return fig

def generate_table(year, max_rows = 10):
    tdata = data.loc[data.year == year, :].copy()
    tdata = tdata.sort_values("lifeExp", ascending = False).iloc[:max_rows, :]
    return tdata.to_dict('records'), [{"name": i, "id": i} for i in tdata.columns]


if __name__ == '__main__':
    app.run_server(debug=True)
