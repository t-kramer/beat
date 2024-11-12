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
                        # html.B(html.Span(id="exp-id-count", className="card-text")),
                        html.Br(),
                        "Total data points: ",
                        # html.B(html.Span(id="data-count", className="card-text")),
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


def infocard_experiments():
    return dbc.Card(
        dbc.CardBody(
            [
                html.B("Summary"),
                html.P(
                    [
                        "You have selected ",
                        html.B(html.Span(id="exp-id-count", className="card-text")),
                        " studies with a total of ",
                        html.B(
                            html.Span(id="participant-count", className="card-text")
                        ),
                        " participants, from ",
                        html.B(html.Span(id="country-count", className="card-text")),
                        " countries. Of these studies, ",
                        html.B(
                            html.Span(
                                id="data-availability-count", className="card-text"
                            )
                        ),
                        " openly share their data.",
                        html.Br(),
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
