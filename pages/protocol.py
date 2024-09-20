import dash

import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, callback

import pandas as pd

from utils.webpage_text import TextPageHeading, ChartTitles

from utils.config_file import (
    URLS,
    ElementsIDs,
    PAGE_LAYOUT,
)

from components.charts import box_session_length

dash.register_page(__name__, path=URLS.PROTOCOL.value, order=4)


def layout():
    return dbc.Container(
        dbc.Row(
            children=[
                dcc.Store(id="selected-parameter-store", storage_type="session"),
                dcc.Store(id="filtered-data-store", storage_type="session"),
                dbc.Col(
                    children=[
                        html.Div(
                            id="id-selected-parameter-text",
                            className="mb-3",
                        ),
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.P("Infocard here", className="card-text"),
                                ]
                            ),
                        ),
                    ],
                    width=PAGE_LAYOUT.column_width_secondary.value,
                ),
                dbc.Col(
                    children=[
                        html.H4(TextPageHeading.protocol.value),
                        html.H5("Protocol design"),
                        html.Div(ChartTitles.box_session_length.value),
                        dcc.Graph(
                            id=ElementsIDs.CHART_BOX_SESSION_LENGTH.value,
                        ),
                    ],
                    width=PAGE_LAYOUT.column_width_primary.value,
                ),
            ]
        )
    )


# update graphs
@callback(
    Output(ElementsIDs.CHART_BOX_SESSION_LENGTH.value, "figure"),
    [Input("filtered-data-store", "data")],
)
def update_charts(data):
    if data is None:
        raise dash.exceptions.PreventUpdate

    df = pd.read_json(data, orient="split")
    return box_session_length(df)
