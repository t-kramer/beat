import dash

from io import StringIO

import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, callback

import pandas as pd

from utils.webpage_text import TextPageHeading, ChartTitles

from utils.config_file import (
    URLS,
    ElementsIDs,
    PAGE_LAYOUT,
)

from components.charts import (
    box_session_length,
    box_normalisation_length,
    scatter_test_temp,
    heatmap_protocol,
    heatmap_selection,
)

from components.infocard import infocard

dash.register_page(__name__, path=URLS.PROTOCOL.value, order=5)


def layout():
    return dbc.Container(
        [
            dbc.Row(
                children=[
                    dcc.Store(id="filtered-data-store", storage_type="session"),
                    html.H4(TextPageHeading.protocol.value),
                ]
            ),
            dbc.Row(
                children=[
                    dbc.Col(
                        children=[
                            infocard(),
                        ],
                        width=PAGE_LAYOUT.column_width_secondary.value,
                    ),
                    dbc.Col(
                        children=[
                            dbc.Label(ChartTitles.heatmap_protocol.value),
                            dcc.Loading(
                                type=ElementsIDs.LOADING_TYPE.value,
                                children=dcc.Graph(
                                    id=ElementsIDs.CHART_HEATMAP_PROTOCOL.value,
                                ),
                            ),
                        ],
                        width=PAGE_LAYOUT.column_width_primary.value,
                    ),
                ]
            ),
            dbc.Row(
                children=[
                    dbc.Col(
                        children=[
                            infocard(),
                        ],
                        width=PAGE_LAYOUT.column_width_secondary.value,
                    ),
                    dbc.Col(
                        children=[
                            dbc.Label(ChartTitles.heatmap_selection.value),
                            dcc.Loading(
                                type=ElementsIDs.LOADING_TYPE.value,
                                children=dcc.Graph(
                                    id=ElementsIDs.CHART_HEATMAP_SELECTION.value,
                                ),
                            ),
                        ],
                        width=PAGE_LAYOUT.column_width_primary.value,
                    ),
                ]
            ),
            dbc.Row(
                children=[
                    dbc.Col(
                        children=[
                            infocard(),
                        ],
                        width=PAGE_LAYOUT.column_width_secondary.value,
                    ),
                    dbc.Col(
                        children=[
                            dcc.Loading(
                                type=ElementsIDs.LOADING_TYPE.value,
                                children=dcc.Graph(
                                    id=ElementsIDs.CHART_SCATTER_TEST_TEMPS.value,
                                ),
                            ),
                        ],
                        width=PAGE_LAYOUT.column_width_primary.value,
                    ),
                ]
            ),
            dbc.Row(
                children=[
                    dbc.Col(
                        children=[
                            infocard(),
                        ],
                        width=PAGE_LAYOUT.column_width_secondary.value,
                    ),
                    dbc.Col(
                        children=[
                            dbc.Label(ChartTitles.box_session_length.value),
                            dcc.Loading(
                                type=ElementsIDs.LOADING_TYPE.value,
                                children=dcc.Graph(
                                    id=ElementsIDs.CHART_BOX_SESSION_LENGTH.value,
                                ),
                            ),
                        ],
                        width=PAGE_LAYOUT.column_width_primary.value,
                    ),
                ]
            ),
            dbc.Row(
                children=[
                    dbc.Col(
                        children=[
                            infocard(),
                        ],
                        width=PAGE_LAYOUT.column_width_secondary.value,
                    ),
                    dbc.Col(
                        children=[
                            dbc.Label(ChartTitles.box_normalisation_length.value),
                            dcc.Loading(
                                type=ElementsIDs.LOADING_TYPE.value,
                                children=dcc.Graph(
                                    id=ElementsIDs.CHART_BOX_NORMALISATION_LENGTH.value,
                                ),
                            ),
                        ],
                        width=PAGE_LAYOUT.column_width_primary.value,
                    ),
                ]
            ),
        ]
    )


# update graphs
@callback(
    Output(ElementsIDs.CHART_HEATMAP_PROTOCOL.value, "figure"),
    Output(ElementsIDs.CHART_HEATMAP_SELECTION.value, "figure"),
    Output(ElementsIDs.CHART_SCATTER_TEST_TEMPS.value, "figure"),
    Output(ElementsIDs.CHART_BOX_SESSION_LENGTH.value, "figure"),
    Output(ElementsIDs.CHART_BOX_NORMALISATION_LENGTH.value, "figure"),
    [Input("filtered-data-store", "data")],
)
def update_charts(data):
    if data is None:
        raise dash.exceptions.PreventUpdate

    json_data = StringIO(data)
    filtered_df = pd.read_json(json_data, orient="split")

    return (
        heatmap_protocol(filtered_df),
        heatmap_selection(filtered_df),
        scatter_test_temp(filtered_df),
        box_session_length(filtered_df),
        box_normalisation_length(filtered_df),
    )
