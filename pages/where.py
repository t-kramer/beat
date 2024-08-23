import dash

import dash_bootstrap_components as dbc
from dash import dcc
from dash import Dash, dcc, html, Input, Output, callback

from utils.config_file import (
    URLS,
    ElementsIDs,
)

from components.charts import body_site_map
from components.tabs import standard_tab_layout

dash.register_page(__name__, path=URLS.WHERE.value, order=2)


def layout():
    return standard_tab_layout(body_site_map())
