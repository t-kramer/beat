import dash
from dash import dcc, html

import dash_bootstrap_components as dbc

from components.input import standard_dropdown

from utils.config_file import (
    PAGE_LAYOUT,
)


def standard_tab_layout(page_heading, figures: list):

    graph_components = [dcc.Graph(figure=fig) for fig in figures]

    return dbc.Container(
        children=[
            dbc.Row(
                children=[
                    dbc.Col(
                        standard_dropdown(),
                        width=PAGE_LAYOUT.column_width_secondary.value,
                    ),
                    dbc.Col(dbc.Container(html.H4(page_heading))),
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
                        align=PAGE_LAYOUT.infocard_align.value,
                        width=PAGE_LAYOUT.column_width_secondary.value,
                    ),
                    dbc.Col(
                        dbc.Row(
                            children=graph_components,
                        ),
                        width=PAGE_LAYOUT.column_width_primary.value,
                    ),
                ]
            ),
        ]
    )


def grid_tab_layout(page_heading, figures: list):
    graph_components = [dcc.Graph(figure=fig) for fig in figures]

    def get_graph_component(index):
        return (
            graph_components[index] if index < len(graph_components) else html.Div()
        )  # in case there are less than 4 figures

    return dbc.Container(
        children=[
            dbc.Row(
                children=[
                    dbc.Col(
                        standard_dropdown(),
                        width=PAGE_LAYOUT.column_width_secondary.value,
                    ),
                    dbc.Col(dbc.Container(html.H4(page_heading))),
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
                        align=PAGE_LAYOUT.infocard_align.value,
                        width=PAGE_LAYOUT.column_width_secondary.value,
                    ),
                    dbc.Col(
                        get_graph_component(0),
                        width=PAGE_LAYOUT.column_width_grid.value,
                    ),
                    dbc.Col(
                        get_graph_component(1),
                        width=PAGE_LAYOUT.column_width_grid.value,
                    ),
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
                        align=PAGE_LAYOUT.infocard_align.value,
                        width=PAGE_LAYOUT.column_width_secondary.value,
                    ),
                    dbc.Col(
                        dbc.Row(
                            children=get_graph_component(2),
                        ),
                        width=PAGE_LAYOUT.column_width_grid.value,
                    ),
                    dbc.Col(
                        dbc.Row(
                            children=get_graph_component(3),
                        ),
                        width=PAGE_LAYOUT.column_width_grid.value,
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
