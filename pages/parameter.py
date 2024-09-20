import pandas as pd
import plotly.express as px

import dash

import dash_bootstrap_components as dbc
from dash import dcc
from dash import dcc, html, Input, Output, State, callback

from components.charts import bar_year, map_country, pie_building_type
from components.data_table import data_table
from components.input import parameter_checklist

from utils.config_file import PAGE_LAYOUT, URLS, ElementsIDs, LABELS

from utils.webpage_text import TextInfo

dash.register_page(__name__, path=URLS.PARAMETER.value, order=1)


df = pd.read_csv("./data/test.csv")


def layout():
    return dbc.Container(
        children=[
            dcc.Store(id="selected-parameter-store", storage_type="session"),
            dcc.Store(id="filtered-data-store", storage_type="session"),
            dbc.Row(
                children=[
                    dbc.Col(
                        children=[
                            dbc.Row(
                                children=[
                                    html.B("Quick selection:"),
                                    html.Div(
                                        "Use this tab to select the parameter you want to explore."
                                    ),
                                    parameter_checklist(),
                                ],
                            ),
                        ],
                        width=PAGE_LAYOUT.column_width_secondary.value,
                    ),
                    dbc.Col(
                        dbc.Tabs(
                            [
                                dbc.Tab(
                                    dcc.Graph(
                                        id=ElementsIDs.CHART_BAR_YEAR.value,
                                        figure=bar_year(df),
                                    ),
                                    label=LABELS.BY_YEAR.value,
                                ),
                                dbc.Tab(
                                    dcc.Graph(
                                        id=ElementsIDs.CHART_MAP_COUNTRY.value,
                                        figure=map_country(df),
                                    ),
                                    label=LABELS.BY_COUNTRY.value,
                                ),
                                dbc.Tab(
                                    dcc.Graph(
                                        id=ElementsIDs.CHART_PIE_BUILDING_TYPE.value,
                                        figure=pie_building_type(df),
                                    ),
                                    label=LABELS.BY_BUILDING_TYPE.value,
                                ),
                            ]
                        ),
                        width=PAGE_LAYOUT.column_width_primary.value,
                    ),
                ]
            ),
            dbc.Row(
                children=[
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.B("Summary"),
                                    html.P(
                                        "Use this card to summarise information from table "
                                        "in a few lines.",
                                    ),
                                ]
                            ),
                        ),
                        width=PAGE_LAYOUT.column_width_secondary.value,
                    ),
                    dbc.Col(
                        data_table(df), width=PAGE_LAYOUT.column_width_primary.value
                    ),
                ]
            ),
        ]
    )


@callback(
    Output("parameter_checklist", "value"),
    Input("selected-parameter-store", "data"),
    State("parameter_checklist", "value"),
)
def load_checklist_state(saved_data, current_value):
    if saved_data is None:
        return current_value  # Return current value if no stored data
    return saved_data


@callback(
    [
        Output(ElementsIDs.CHART_BAR_YEAR.value, "figure"),
        Output(ElementsIDs.CHART_MAP_COUNTRY.value, "figure"),
        Output(ElementsIDs.CHART_PIE_BUILDING_TYPE.value, "figure"),
        Output("filtered-data-store", "data"),
        Output("selected-parameter-store", "data"),
    ],
    [Input("parameter_checklist", "value")],
)
def update_graphs(selected_parameters):
    filtered_df = df[df["physio-parameter"].isin(selected_parameters)]

    print(selected_parameters)  #! Remove later

    bar_year_fig = bar_year(filtered_df)
    map_country_fig = map_country(filtered_df)
    pie_building_type_fig = pie_building_type(filtered_df)

    filtered_df_json = filtered_df.to_json(date_format="iso", orient="split")

    return (
        bar_year_fig,
        map_country_fig,
        pie_building_type_fig,
        filtered_df_json,
        selected_parameters,
    )


@callback(
    Output("id-selected-parameter-text", "children"),
    [Input("selected-parameter-store", "data")],
)
def update_infocard(selected_parameters):
    if selected_parameters is None:
        raise dash.exceptions.PreventUpdate

    return dbc.Container(
        children=[
            html.B(TextInfo.selected_parameters.value),
            html.Div(
                [
                    html.Div(param, className="parameter-item")
                    for param in selected_parameters
                ]
            ),
        ]
    )
