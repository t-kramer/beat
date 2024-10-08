import dash

import pandas as pd

import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, callback

from components.charts import (
    bar_thermal_questionnaires,
    parallel__questionnaires_scales,
)

from utils.webpage_text import TextPageHeading, ChartTitles

from utils.config_file import URLS, ElementsIDs, PAGE_LAYOUT

from components.infocard import infocard

dash.register_page(__name__, path=URLS.QUESTIONNAIRE.value, order=5)


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
                        html.H4(TextPageHeading.questionnaire.value),
                        html.Div(ChartTitles.bar_thermal_questionnaire.value),
                        dcc.Graph(
                            id=ElementsIDs.CHART_BAR_THERMAL_QUESTIONNAIRE.value,
                        ),
                        html.Div(ChartTitles.parallel_questionnaire_scales.value),
                        dcc.Graph(
                            id=ElementsIDs.CHART_PARALLEL_QUESTIONNAIRE_SCALES.value,
                        ),
                    ],
                    width=PAGE_LAYOUT.column_width_primary.value,
                ),
            ]
        )
    )


# update graphs
@callback(
    Output(ElementsIDs.CHART_PARALLEL_QUESTIONNAIRE_SCALES.value, "figure"),
    Output(ElementsIDs.CHART_BAR_THERMAL_QUESTIONNAIRE.value, "figure"),
    [Input("filtered-data-store", "data")],
)
def update_charts(data):
    if data is None:
        raise dash.exceptions.PreventUpdate

    df = pd.read_json(data, orient="split")
    return parallel__questionnaires_scales(df), bar_thermal_questionnaires(df)
