import dash

import dash_bootstrap_components as dbc
from dash import dcc
from dash import Dash, dcc, html, Input, Output, callback

from utils.config_file import (
    URLS,
    ElementsIDs,
)

from components.tabs import grid_tab_layout
from components.data import load_data
from components.charts import box_number_participants, pie_age, violin_sex

dash.register_page(__name__, path=URLS.WHO.value, order=4)

df = load_data()


def layout():
    return grid_tab_layout([box_number_participants(df), pie_age(df), violin_sex(df)])
