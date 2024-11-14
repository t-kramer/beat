import dash

from io import StringIO

import dash_bootstrap_components as dbc
from dash import dcc
from dash import dcc, html, Input, Output, callback

import pandas as pd

from utils.webpage_text import TextPageHeading, ChartTitles

from utils.config_file import (
    URLS,
    ElementsIDs,
    PAGE_LAYOUT,
)

from components.charts import box_number_participants, pie_age, histogram_sex

from components.infocard import infocard

dash.register_page(__name__, path=URLS.PARTICIPANTS.value, order=4)


def layout():
    return dbc.Container(
        [
            dbc.Row(
                children=[
                    html.H4(TextPageHeading.participants.value),
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
                            dbc.Label(ChartTitles.box_no_participants.value),
                            dcc.Loading(
                                type=ElementsIDs.LOADING_TYPE.value,
                                children=dcc.Graph(
                                    id=ElementsIDs.CHART_BOX_NO_PARTICIPANTS.value,
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
                            dbc.Label(ChartTitles.chart_pie_age.value),
                            dcc.Loading(
                                type=ElementsIDs.LOADING_TYPE.value,
                                children=dcc.Graph(
                                    id=ElementsIDs.CHART_PIE_AGE.value,
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
                            dbc.Label(ChartTitles.chart_histogram_sex.value),
                            dcc.Loading(
                                type=ElementsIDs.LOADING_TYPE.value,
                                children=dcc.Graph(
                                    id=ElementsIDs.CHART_HISTOGRAM_SEX.value,
                                ),
                            ),
                        ],
                        width=PAGE_LAYOUT.column_width_primary.value,
                    ),
                ]
            ),
        ]
    )


@callback(
    Output(ElementsIDs.CHART_BOX_NO_PARTICIPANTS.value, "figure"),
    Output(ElementsIDs.CHART_PIE_AGE.value, "figure"),
    Output(ElementsIDs.CHART_HISTOGRAM_SEX.value, "figure"),
    [Input(ElementsIDs.STORE_DATA.value, "data")],
)
def update_charts(data):
    if data is None:
        raise dash.exceptions.PreventUpdate

    json_data = StringIO(data)
    filtered_df = pd.read_json(json_data, orient="split")

    return (
        box_number_participants(filtered_df),
        pie_age(filtered_df),
        histogram_sex(filtered_df),
    )
