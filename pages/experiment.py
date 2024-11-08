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

from utils.webpage_text import TextInfo, FilterText

dash.register_page(__name__, path=URLS.EXPERIMENT.value, order=1)


df = pd.read_csv("./data/test.csv")


def layout():
    return dbc.Container(
        children=[
            dcc.Store(id="filter-selection-store", storage_type="session"),
            dcc.Store(id="filtered-data-store", storage_type="session"),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Label(FilterText.study_type.value),
                            study_type_checklist(),
                            html.Hr(),
                            dbc.Label(FilterText.country.value),
                            country_dropdown(),
                        ],
                        width=4,
                    ),
                    dbc.Col(
                        [
                            dbc.Label(FilterText.building_typology.value),
                            building_typology_checklist(),
                            html.Hr(),
                            dbc.Label(FilterText.year.value),
                            year_slider(df["pub-year"].min(), df["pub-year"].max()),
                        ],
                        width=5,
                    ),
                    dbc.Col(
                        [
                            dbc.Label(FilterText.physiological_parameters.value),
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
                        ],
                        width=PAGE_LAYOUT.column_width_primary.value,
                    ),
                ]
            ),
            dbc.Row(
                dbc.Col(
                    [
                        dbc.Label(FilterText.data_table.value),
                        data_table(df),
                    ],
                )
            ),
        ]
    )


# 1.) Set options and values based on initial data
@callback(
    [
        Output("study-type-checklist", "options"),
        Output("study-type-checklist", "value"),
        Output("building-typology-checklist", "options"),
        Output("building-typology-checklist", "value"),
        Output("country-dropdown", "options"),
        Output("country-dropdown", "value"),
        Output("year-slider", "value"),
        Output("year-slider", "min"),
        Output("year-slider", "max"),
        Output("year-slider", "marks"),
    ],
    [Input("initial-load", "children")],
)
def set_filter_options(_):

    def generate_options_and_values(column):
        unique_values = sorted(df[column].dropna().unique(), reverse=True)
        options = [{"label": i, "value": i} for i in unique_values]
        return options, unique_values

    # options and values for each checklist and dropdown
    study_type_options, study_values = generate_options_and_values("exp-type")
    typology_options, typology_values = generate_options_and_values("function")
    country_options, country_values = generate_options_and_values("country")

    # slider settings
    year_min = df["pub-year"].min()
    year_max = df["pub-year"].max()
    year_marks = {year: str(year) for year in range(year_min, year_max + 1)}
    years_options = [year_min, year_max]

    print("initial options and values set!")  #! Remove later

    return (
        study_type_options,
        study_values,
        typology_options,
        typology_values,
        country_options,
        country_values,
        years_options,
        year_min,
        year_max,
        year_marks,
    )


# 2.) Store filters when updated
@callback(
    Output("filter-selection-store", "data"),
    [
        Input("parameter-checklist", "value"),
        Input("study-type-checklist", "value"),
        Input("building-typology-checklist", "value"),
        Input("country-dropdown", "value"),
        Input("year-slider", "value"),
    ],
)
def store_selected_filters(parameters, study_type, typology, country, years):

    selected_filters = {
        "parameters_value": parameters,
        "study_type_value": study_type,
        "building_typology_value": typology,
        "country_value": country,
        "years_value": years,
    }

    print("filters saved!")  #! Remove later

    return selected_filters  # ? filter-selection-store


# 3.) Filter data based on selected filters and store it
@callback(
    [
        Output("filtered-data-store", "data"),
    ],
    [
        Input("filter-selection-store", "data"),
    ],
)
def filter_data(loaded_filters):

    min_year, max_year = loaded_filters["years_value"]
    all_years = list(range(min_year, max_year + 1))

    parameters = loaded_filters["parameters_value"]
    study_type = loaded_filters["study_type_value"]
    typology = loaded_filters["building_typology_value"]
    country = loaded_filters["country_value"]

    filtered_df = df[
        (df["physio-parameter"].isin(parameters))
        & (df["exp-type"].isin(study_type or df["exp-type"].unique()))
        & (df["function"].isin(typology or df["function"].unique()))
        & (df["country"].isin(country or df["country"].unique()))
        & (df["pub-year"].isin(all_years))
    ]

    print("filtered data saved!")

    filtered_df_json = filtered_df.to_json(date_format="iso", orient="split")

    return (filtered_df_json,)  # ? filtered-data-store


# 4.) Update graphs and data table based on filtered data
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
    if data is None:
        return dash.no_update  # Skip update if no data is stored
    try:
        json_data = StringIO(data)
        filtered_df = pd.read_json(json_data, orient="split")
    except Exception as e:
        print(f"Error loading data from store: {e}")
        return dash.no_update

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
# def load_checklist_state(loaded_data, current_value):
#     if loaded_data is None:
#         return current_value  # Return current value if no stored data
#     return loaded_data


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
