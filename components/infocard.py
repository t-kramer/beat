from dash import html

import pandas as pd

import dash_bootstrap_components as dbc


def infocard():
    return dbc.Card(
        dbc.CardBody(
            [
                html.B("Summary"),
                html.P(
                    [
                        "No. Experiments: ",
                        html.B(html.Span(id="exp-id-count", className="card-text")),
                    ],
                    className="card-text",
                ),
            ]
        ),
    )
