import pandas as pd
import plotly.express as px
from io import StringIO

import dash

import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State, callback

from components.charts import bar_year, map_country, pie_building_type
from components.data_table import data_table
from components.input import (
    parameter_checklist,
    study_type_checklist,
    country_dropdown,
    building_typology_checklist,
    year_slider,
)

from utils.config_file import PAGE_LAYOUT, URLS, ElementsIDs, LABELS

from utils.webpage_text import TextInfo

dash.register_page(__name__, path=URLS.EXPERIMENT.value, order=1)


df = pd.read_csv("./data/test.csv")


def layout():
    return dbc.Container(
        children=[
            dcc.Store(id="selected-parameter-store", storage_type="session"),
            dcc.Store(id="filtered-data-store", storage_type="session"),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Label("Study Type."),
                            study_type_checklist(),
                            dbc.Label("Country."),
                            country_dropdown(),
                        ],
                        width=4,
                    ),
                    dbc.Col(
                        [
                            dbc.Label("Building Typology."),
                            building_typology_checklist(),
                            dbc.Label("Year"),
                            year_slider(df["pub-year"].min(), df["pub-year"].max()),
                        ],
                        width=5,
                    ),
                    dbc.Col(
                        [
                            dbc.Label("Physiological Parameters."),
                            parameter_checklist(),
                        ],
                        width=PAGE_LAYOUT.column_width_secondary.value,
                    ),
                ]
            ),
            html.Hr(),
            dbc.Row(
                children=[
                    dbc.Col(
                        children=[
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
                        ],
                        width=PAGE_LAYOUT.column_width_secondary.value,
                    ),
                    dbc.Col(
                        children=[
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
                            dbc.Label("List of filtered studies."),
                            data_table(df),
                        ],
                        width=PAGE_LAYOUT.column_width_primary.value,
                    ),
                ]
            ),
        ]
    )


# update dropdown options dynamically
@callback(
    [
        Output("study-type-checklist", "options"),
        Output("building-typology-checklist", "options"),
        Output("country-dropdown", "options"),
        Output("year-slider", "min"),
        Output("year-slider", "max"),
        Output("year-slider", "marks"),
        # Output("parameter_checklist", "value"),
    ],
    Input("filtered-data-store", "data"),
)
def update_filter_options(_):
    # Extract dropwdown options
    study_type_options = [
        {"label": i, "value": i}
        for i in sorted(df["exp-type"].dropna().unique(), reverse=True)
    ]
    typology_options = [
        {"label": i, "value": i} for i in sorted(df["function"].dropna().unique())
    ]
    country_options = [
        {"label": i, "value": i} for i in sorted(df["country"].dropna().unique())
    ]

    year_min = df["pub-year"].min()
    year_max = df["pub-year"].max()
    year_marks = {i: str(i) for i in range(year_min, year_max + 1, 1)}

    return (
        study_type_options,
        typology_options,
        country_options,
        year_min,
        year_max,
        year_marks,
    )


@callback(
    [
        Output("filtered-data-store", "data"),
    ],
    [
        Input("parameter-checklist", "value"),
        Input("study-type-checklist", "value"),
        Input("building-typology-checklist", "value"),
        Input("country-dropdown", "value"),
        Input("year-slider", "value"),
    ],
)
def filter_data(parameters, study_type, typology, country, years):

    min_year, max_year = years
    all_years = list(range(min_year, max_year + 1))

    print(parameters, study_type, typology, country, all_years)  #! Remove later
    filtered_df = df[
        (df["physio-parameter"].isin(parameters))
        & (df["exp-type"].isin(study_type or df["exp-type"].unique()))
        & (df["function"].isin(typology or df["function"].unique()))
        & (df["country"].isin(country or df["country"].unique()))
        & (df["pub-year"].isin(all_years))
    ]

    filtered_df_json = filtered_df.to_json(date_format="iso", orient="split")

    return (filtered_df_json,)


@callback(
    [
        Output(ElementsIDs.CHART_BAR_YEAR.value, "figure"),
        Output(ElementsIDs.CHART_MAP_COUNTRY.value, "figure"),
        Output(ElementsIDs.CHART_PIE_BUILDING_TYPE.value, "figure"),
        Output("data-table", "data"),
    ],
    [Input("filtered-data-store", "data")],
)
def update_graphs_datatable(data):

    json_data = StringIO(data)
    filtered_df = pd.read_json(json_data, orient="split")

    bar_year_fig = bar_year(filtered_df)
    map_country_fig = map_country(filtered_df)
    pie_building_type_fig = pie_building_type(filtered_df)

    updated_table_data = filtered_df.drop_duplicates(subset=["exp-id"]).sort_values(
        by="pub-year", ascending=True, inplace=False
    )

    return (
        bar_year_fig,
        map_country_fig,
        pie_building_type_fig,
        updated_table_data.to_dict("records"),
    )


# @callback(
#     Output("parameter_checklist", "value"),
#     Input("selected-parameter-store", "data"),
#     State("parameter_checklist", "value"),
# )
# def load_checklist_state(saved_data, current_value):
#     if saved_data is None:
#         return current_value  # Return current value if no stored data
#     return saved_data


# @callback(
#     Output("id-selected-parameter-text", "children"),
#     [Input("selected-parameter-store", "data")],
# )
# def update_infocard(selected_parameters):
#     if selected_parameters is None:
#         raise dash.exceptions.PreventUpdate

#     return dbc.Container(
#         children=[
#             html.B(TextInfo.selected_parameters.value),
#             html.Div(
#                 [
#                     html.Div(param, className="parameter-item")
#                     for param in selected_parameters
#                 ]
#             ),
#         ]
#     )
