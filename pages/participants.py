import dash

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

from components.charts import box_number_participants, pie_age, violin_sex

from components.infocard import infocard

dash.register_page(__name__, path=URLS.PARTICIPANTS.value, order=3)


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
                        html.H4(TextPageHeading.participant.value),
                        html.Div(ChartTitles.box_no_participants.value),
                        dcc.Graph(
                            id=ElementsIDs.CHART_BOX_NO_PARTICIPANTS.value,
                        ),
                        html.Div(ChartTitles.chart_pie_age.value),
                        dcc.Graph(
                            id=ElementsIDs.CHART_PIE_AGE.value,
                        ),
                        html.Div(ChartTitles.chart_violin_sex.value),
                        dcc.Graph(
                            id=ElementsIDs.CHART_VIOLIN_SEX.value,
                        ),
                    ],
                    width=PAGE_LAYOUT.column_width_primary.value,
                ),
            ]
        )
    )


# update graphs
@callback(
    Output(ElementsIDs.CHART_BOX_NO_PARTICIPANTS.value, "figure"),
    Output(ElementsIDs.CHART_PIE_AGE.value, "figure"),
    Output(ElementsIDs.CHART_VIOLIN_SEX.value, "figure"),
    [Input("filtered-data-store", "data")],
)
def update_charts(data):
    if data is None:
        raise dash.exceptions.PreventUpdate

    df = pd.read_json(data, orient="split")
    return box_number_participants(df), pie_age(df), violin_sex(df)
