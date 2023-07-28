from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
from app import *
from components import sidebar, dashboards, investimentos


# ===== LAYOUT ====== #
content = html.Div(id="page-content")

app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id="url"),
            sidebar.layout
        ], md=2),

        dbc.Col([
            content
        ], md=10),
    ])

], fluid=True,)

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/" or pathname == "/dashboards":
        return dashboards.layout
    
    if pathname == "/investimentos":
        return investimentos.layout


if __name__ == '__main__':
    app.run_server(port=8051,  debug=True)