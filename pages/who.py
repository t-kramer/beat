import dash

import dash_bootstrap_components as dbc
from dash import dcc
from dash import Dash, dcc, html, Input, Output, callback

from utils.config_file import (
    URLS,
    ElementsIDs,
)

from components.tabs import standard_tab_layout

dash.register_page(__name__, path=URLS.WHO.value, order=4)


def layout():
    return standard_tab_layout([])
