import dash
from dash import dcc, html

import dash_bootstrap_components as dbc

from components.input import standard_dropdown

from utils.config_file import (
    Dimensions,
)


def standard_tab_layout(figures: list):

    graph_components = [dcc.Graph(figure=fig) for fig in figures]

    return dbc.Container(
        children=[
            dbc.Row(
                children=[
                    dbc.Col(
                        standard_dropdown(),
                        width=Dimensions.column_width_secondary.value,
                    ),
                    dbc.Col(dbc.Container()),
                ]
            ),
            dbc.Row(
                children=[
                    dbc.Col(
                        children=[
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.P("Infocard here", className="card-text"),
                                    ]
                                ),
                            )
                        ],
                        align="center",
                        width=Dimensions.column_width_secondary.value,
                    ),
                    dbc.Col(
                        dbc.Row(
                            children=graph_components,
                        ),
                        width=Dimensions.column_width_primary.value,
                    ),
                ]
            ),
        ]
    )


def tabs():
    return dbc.Container(
        children=[
            dbc.Row(
                dbc.Nav(
                    [
                        dbc.NavItem(
                            dbc.NavLink(
                                page["name"],
                                href=page["path"],
                            )
                        )
                        for page in dash.page_registry.values()
                    ],
                ),
            ),
            html.Hr(),
            dbc.Row(dash.page_container),
        ]
    )
