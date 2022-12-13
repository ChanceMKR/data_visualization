# -*- coding: utf-8 -*-

import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import plotly.io as pio
import os
from pathlib import Path
os.chdir(r"C:\Users\Beom\OneDrive - UOS\22년도 강의자료\22년도 데이터 시각화 강의자료\dashboard")
pio.renderers.default = "browser"
data = pd.read_csv("./user_log.csv")
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

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

fig1.update_layout(
    plot_bgcolor = colors["background"],
    paper_bgcolor = colors["background"],
    font_color = colors["text"]
    )
fig2.update_layout(
    plot_bgcolor = colors["background"],
    paper_bgcolor = colors["background"],
    font_color = colors["text"]
    )


app = dash.Dash()

app.layout = html.Div(style = {"backgroundColor" : "#34495E"}, children = [
    html.H1(style = {"textAlign" : "center", 
                     "color" : "#FFFFFF",
                     "fontSize" : 20}, children = "Dashboard for Game-User Data"),
    html.Div(style = {"width": "49%", "display": "inline-block"}, 
             children = [dcc.Graph(id = "month-vs-nlog", figure = fig1)]),
    html.Div(style = {"width": "49%", "display": "inline-block"}, 
             children = [dcc.Graph(id = "month-vs-sum", figure = fig2)])])

if __name__ == "__main__":
    app.run_server(debug=True)
    # app.run_server(debug=False)