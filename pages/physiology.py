import dash
import pandas as pd

import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, callback

from utils.config_file import URLS, ElementsIDs, PAGE_LAYOUT

from utils.webpage_text import TextPageHeading, ChartTitles

from components.charts import (
    sunburst_sensors,
    body_site_map,
    hor_bar_environmental_parameters,
)

from components.infocard import infocard

dash.register_page(__name__, path=URLS.PHYSIOLOGY.value, order=2)


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
                        infocard(),
                    ],
                    width=PAGE_LAYOUT.column_width_secondary.value,
                ),
                dbc.Col(
                    children=[
                        html.H4(TextPageHeading.measurement.value),
                        html.Div(ChartTitles.body_site_map.value),
                        dcc.Graph(
                            id=ElementsIDs.CHART_MAP_BODY.value,
                        ),
                        html.Div(ChartTitles.sunburst_sensors.value),
                        dcc.Graph(
                            id=ElementsIDs.CHART_SUNBURST.value,
                        ),
                        html.Div(ChartTitles.bar_environmental.value),
                        dcc.Graph(
                            id=ElementsIDs.CHART_BAR_ENVIRONMENTAL.value,
                        ),
                    ],
                    width=PAGE_LAYOUT.column_width_primary.value,
                ),
            ]
        )
    )


# update graphs
@callback(
    Output(ElementsIDs.CHART_MAP_BODY.value, "figure"),
    Output(ElementsIDs.CHART_SUNBURST.value, "figure"),
    Output(ElementsIDs.CHART_BAR_ENVIRONMENTAL.value, "figure"),
    [Input("filtered-data-store", "data")],
)
def update_charts(data):
    if data is None:
        raise dash.exceptions.PreventUpdate

    df = pd.read_json(data, orient="split")
    return body_site_map(df), sunburst_sensors(df), hor_bar_environmental_parameters(df)


@callback(
    Output("exp-id-count", "children"),
    Output("data-count", "children"),
    [Input("filtered-data-store", "data")],
)
def update_infocard(data):
    df = pd.read_json(data, orient="split")
    unique_exp_ids = df["exp-id"].nunique()
    total_data_points = len(df)

    return unique_exp_ids, total_data_points
