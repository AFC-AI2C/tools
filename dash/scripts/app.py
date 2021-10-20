from dash.dependencies import Input, Output
from dash import Dash
from dash import dcc
from dash import html

from os import getenv

import pandas as pd
import time


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/hello-world-stock.csv"
)

# When you edit this file, do not touch the `url_base_pathname`, that is
# required for dash deployed on COEUS to be properly found.
app = Dash(
    "app",
    url_base_pathname=f'/{getenv("TOOL_SLUG", default="")}/'.replace("//", "/"),
)

dcc._js_dist[0][
    "external_url"
] = "https://cdn.plot.ly/plotly-basic-latest.min.js"

app.layout = html.Div(
    [
        html.H1("Stock Tickers"),
        dcc.Dropdown(
            id="my-dropdown",
            options=[
                {"label": "Tesla", "value": "TSLA"},
                {"label": "Apple", "value": "AAPL"},
                {"label": "Coke", "value": "COKE"},
            ],
            value="TSLA",
        ),
        dcc.Graph(id="my-graph"),
    ],
    className="container",
)


@app.callback(Output("my-graph", "figure"), [Input("my-dropdown", "value")])
def update_graph(selected_dropdown_value):
    dff = df[df["Stock"] == selected_dropdown_value]
    return {
        "data": [
            {
                "x": dff.Date,
                "y": dff.Close,
                "line": {"width": 3, "shape": "spline"},
            }
        ],
        "layout": {"margin": {"l": 30, "r": 20, "b": 30, "t": 20}},
    }


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
