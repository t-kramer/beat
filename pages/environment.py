import pandas as pd
import plotly.express as px
from io import StringIO

import dash

import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, callback


from utils.config_file import PAGE_LAYOUT, URLS, ElementsIDs, LABELS


from utils.webpage_text import TextInfo, TextPageHeading, ChartTitles

from components.infocard import infocard

from components.charts import (
    hor_bar_environmental_parameters,
)


dash.register_page(__name__, path=URLS.ENVIRONMENT.value, order=3)


def layout():
    return dbc.Container(
        [
            dbc.Row(
                dbc.Col(
                    children=[
                        html.H4(TextPageHeading.environment.value),
                    ]
                ),
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
                            dbc.Label(ChartTitles.bar_environmental.value),
                            dcc.Loading(
                                type=ElementsIDs.LOADING_TYPE.value,
                                children=dcc.Graph(
                                    id=ElementsIDs.CHART_BAR_ENVIRONMENTAL.value
                                ),
                            ),
                        ],
                        width=PAGE_LAYOUT.column_width_primary.value,
                    ),
                ],
            ),
        ],
    )


@callback(
    Output(ElementsIDs.CHART_BAR_ENVIRONMENTAL.value, "figure"),
    [Input(ElementsIDs.STORE_DATA.value, "data")],
)
def update_charts(data):
    if data is None:
        raise dash.exceptions.PreventUpdate

    json_data = StringIO(data)
    filtered_df = pd.read_json(json_data, orient="split")

    return hor_bar_environmental_parameters(filtered_df)
