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
                        html.Br(),
                        "Total data points: ",
                        html.B(html.Span(id="data-count", className="card-text")),
                    ],
                    className="card-text",
                ),
                html.Div(
                    [
                        dbc.CardLink(
                            "GitBook",
                            href="https://github.com/t-kramer/beat",
                            target="_blank",
                            id="tooltip-link",
                        ),
                        dbc.Tooltip(
                            "Get more information on these parameters",
                            target="tooltip-link",
                            placement="top",
                        ),
                    ],
                    style={"display": "flex", "align-items": "center"},
                ),
            ]
        ),
    )
