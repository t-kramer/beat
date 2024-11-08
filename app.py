import os

import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, callback


from components.header import cbe_header
from components.tabs import tabs
from components.footer import cbe_footer

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[
        dbc.themes.LUX,
        "https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap",
    ],
    serve_locally=True,
)

app.layout = dbc.Container(
    fluid=True,
    style={"padding": "0"},
    children=[
        cbe_header(),
        html.Div(
            children=[
                tabs(),
            ],
            style={"padding": "10px"},
        ),
        cbe_footer(),
    ],
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run_server(
        debug=True,
        host="0.0.0.0",
        port=port,
    )
