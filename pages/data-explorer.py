import dash

import dash_bootstrap_components as dbc
from dash import dcc
from dash import Dash, dcc, html, Input, Output, callback

from utils.webpage_text import TextPageHeading

from components.data import load_data

from utils.config_file import (
    URLS,
    ElementsIDs,
)

dash.register_page(
    __name__, path=URLS.DATA_EXPLORER.value, order=6, name="Data Explorer"
)

df = load_data()


def layout():
    return dbc.Container()
