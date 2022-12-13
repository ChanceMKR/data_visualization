# -*- coding: utf-8 -*-

import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
# import os
from pathlib import Path
script_dir = Path(__file__).parent.absolute()
data = pd.read_csv(str(script_dir) + "/user_log.csv")
data.log_date = pd.to_datetime(data.log_date, format = "%Y-%m-%d")
data["month"] = data.log_date.dt.month
n_pay_month = data.groupby(["month"]).payment.agg(["count", "sum"])

n_pay_month = n_pay_month.reset_index(drop = False)
fig1 = px.line(n_pay_month, 
                  x = "month",
                  y = "count")
fig2 = px.line(n_pay_month,
                x = "month",
                y = "sum")

app = dash.Dash()

app.layout = html.Div([
    html.H1("Dashboard for Game-User Data"),
    html.Div("month-vs-# of login"),
    dcc.Graph(id = "month-vs-nlog", figure = fig1),
    html.Div("month-vs-total payment"),
    dcc.Graph(id = "month-vs-sum", figure = fig2)])

if __name__ == "__main__":
    app.run_server(debug=True)
    # app.run_server(debug=False)