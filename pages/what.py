import pandas as pd
import plotly.express as px

import dash

import dash_bootstrap_components as dbc
from dash import dcc
from dash import Dash, dcc, html, Input, Output, callback

from components.charts import bar_year, map_country, pie_building_type
from components.data_table import data_table
from components.input import parameter_checklist

from utils.config_file import Dimensions, URLS, ElementsIDs, LABELS

dash.register_page(__name__, path=URLS.WHAT.value, order=1)


df = pd.read_csv("./data/ulti-dataDict.csv")


def layout():
    return dbc.Container(
        children=[
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
                        width=Dimensions.column_width_secondary.value,
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
                        width=Dimensions.column_width_primary.value,
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
                        width=Dimensions.column_width_secondary.value,
                    ),
                    dbc.Col(
                        data_table(df), width=Dimensions.column_width_primary.value
                    ),
                ]
            ),
        ]
    )


# @callback(
#     [Output(component_id='output_container', component_property='children'),
#      Output(component_id=ElementsIDs.CHART_CONTAINER.value, component_property='figure')],
#     [Input(component_id='select_parameter', component_property='value')]
# )
# def update_graph(parameter_slctd):
#     print(parameter_slctd)
#     print(type(parameter_slctd))

#     container = "The parameter chosen by user was: {}".format(parameter_slctd)

#     dff = df.copy()

#     dff['exp-id'] = dff['exp-id'].astype(str)

#     filtered_dff = dff[dff['physio-parameter'] == parameter_slctd]

#     grouped = filtered_dff.groupby('exp-id').size().reset_index(name='counts')

#     fig = px.histogram(grouped, x='exp-id', y='counts', title=f"Total Count of '{parameter_slctd}' over all 'paper'")

#     return container, fig
