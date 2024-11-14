import pandas as pd
import plotly.express as px
from io import StringIO

import dash

import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State, callback

from components.charts import bar_year, map_country, pie_building_type, bar_data_access
from components.data_table import data_table
from components.input import (
    parameter_checklist,
    study_type_checklist,
    country_dropdown,
    building_typology_checklist,
    year_slider,
)

from components.infocard import infocard_experiments

from utils.config_file import PAGE_LAYOUT, URLS, ElementsIDs, LABELS
from utils.webpage_text import TextInfo, FilterText
from utils.helper_functions import get_unique_studies

dash.register_page(__name__, path=URLS.EXPERIMENT.value, order=1)


df = pd.read_csv("./data/test.csv")


def layout():
    return dbc.Container(
        children=[
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
                            html.Br(),
                            dbc.Button(
                                "Reset Parameters",
                                id=ElementsIDs.BUTTON_RESET_FILTER.value,
                                color="primary",
                            ),
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
                            infocard_experiments(),
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
                                    dbc.Tab(
                                        dcc.Graph(
                                            id=ElementsIDs.CHART_BAR_DATA_AVAILABILITY.value,
                                            figure=bar_data_access(df),
                                        ),
                                        label=LABELS.DATA_ACCESS.value,
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


# 1.) Set options and values based on either initial data or stored filters
@callback(
    [
        Output(ElementsIDs.CHECKLIST_STUDY_TYPE.value, "options"),
        Output(ElementsIDs.CHECKLIST_STUDY_TYPE.value, "value"),
        Output(ElementsIDs.CHECKLIST_BUILDING_TYPOLOGY.value, "options"),
        Output(ElementsIDs.CHECKLIST_BUILDING_TYPOLOGY.value, "value"),
        Output(ElementsIDs.DROPDOWN_COUNTRY.value, "options"),
        Output(ElementsIDs.DROPDOWN_COUNTRY.value, "value"),
        Output(ElementsIDs.CHECKLIST_PARAMETER.value, "options"),
        Output(ElementsIDs.CHECKLIST_PARAMETER.value, "value"),
        Output(ElementsIDs.SLIDER_YEAR.value, "value"),
        Output(ElementsIDs.SLIDER_YEAR.value, "min"),
        Output(ElementsIDs.SLIDER_YEAR.value, "max"),
        Output(ElementsIDs.SLIDER_YEAR.value, "marks"),
    ],
    [Input("initial-load", "children")],
    [State(ElementsIDs.STORE_FILTER.value, "data")],
)
def set_filter_options(_, stored_data):

    def generate_options_and_values(column):
        unique_values = sorted(df[column].dropna().unique(), reverse=True)
        options = [{"label": i, "value": i} for i in unique_values]
        return options, unique_values

    # options and values for each checklist and dropdown
    study_type_options, study_values = generate_options_and_values("exp-type")
    typology_options, typology_values = generate_options_and_values("function")
    country_options, country_values = generate_options_and_values("country")
    parameter_options, parameter_values = generate_options_and_values(
        "physio-parameter"
    )

    # slider settings
    year_min = df["pub-year"].min()
    year_max = df["pub-year"].max()
    year_marks = {year: str(year) for year in range(year_min, year_max + 1)}
    years_values = [year_min, year_max]

    if stored_data is None:

        print("initial options and values set!")  #! Remove later

        return (
            study_type_options,
            study_values,
            typology_options,
            typology_values,
            country_options,
            country_values,
            parameter_options,
            parameter_values,
            years_values,
            year_min,
            year_max,
            year_marks,
        )

    print("previous filters restored!")  #! Remove later

    return (
        study_type_options,
        stored_data["study_type_value"],
        typology_options,
        stored_data["building_typology_value"],
        country_options,
        stored_data["country_value"],
        parameter_options,
        stored_data["parameters_value"],
        stored_data["years_value"],
        year_min,
        year_max,
        year_marks,
    )


# 2.) Store filters when updated
@callback(
    Output(ElementsIDs.STORE_FILTER.value, "data"),
    [
        Input(ElementsIDs.CHECKLIST_PARAMETER.value, "value"),
        Input(ElementsIDs.CHECKLIST_STUDY_TYPE.value, "value"),
        Input(ElementsIDs.CHECKLIST_BUILDING_TYPOLOGY.value, "value"),
        Input(ElementsIDs.DROPDOWN_COUNTRY.value, "value"),
        Input(ElementsIDs.SLIDER_YEAR.value, "value"),
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
        Output(ElementsIDs.STORE_DATA.value, "data"),
    ],
    [
        Input(ElementsIDs.STORE_FILTER.value, "data"),
    ],
)
def filter_data(loaded_filters):
    if loaded_filters is None:
        raise dash.exceptions.PreventUpdate

    years = loaded_filters["years_value"]
    all_years = list(range(min(years), max(years) + 1))

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
        Output(ElementsIDs.CHART_BAR_DATA_AVAILABILITY.value, "figure"),
        Output(ElementsIDs.DATA_TABLE.value, "data"),
        Output(ElementsIDs.DATA_TABLE.value, "tooltip_data"),
    ],
    [Input(ElementsIDs.STORE_DATA.value, "data")],
)
def update_graphs_datatable(data):
    if data is None:
        return dash.no_update

    try:
        json_data = StringIO(data)
        filtered_df = pd.read_json(json_data, orient="split")
    except Exception as e:
        print(f"Error loading data from store: {e}")
        return dash.no_update

    updated_table_data = filtered_df.drop_duplicates(subset=["exp-id"]).sort_values(
        by="pub-year", ascending=True, inplace=False
    )

    # dynamic tooltip data
    tooltip_data = [
        {
            column: {
                "value": str(value) if value is not None else "",
                "type": "markdown",
            }
            for column, value in row.items()
        }
        for row in updated_table_data.to_dict("records")
    ]

    return (
        bar_year(filtered_df),
        map_country(filtered_df),
        pie_building_type(filtered_df),
        bar_data_access(filtered_df),
        updated_table_data.to_dict("records"),
        tooltip_data,
    )


# 5.) Update infocard
@callback(
    Output("exp-id-count", "children"),
    Output("participant-count", "children"),
    Output("country-count", "children"),
    Output("data-availability-count", "children"),
    [Input(ElementsIDs.STORE_DATA.value, "data")],
)
def update_infocard(data):

    json_data = StringIO(data)
    df = pd.read_json(json_data, orient="split")

    unique_studies = get_unique_studies(df)

    unique_exp_ids = len(unique_studies)
    total_data_points = len(df)
    unique_countries = df["country"].nunique()

    unique_studies = get_unique_studies(df)
    data_availability = (unique_studies["data-avail"] == "Available").sum()

    return unique_exp_ids, total_data_points, unique_countries, data_availability
