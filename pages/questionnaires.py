import dash

import dash_bootstrap_components as dbc
from dash import dcc
from dash import Dash, dcc, html, Input, Output, callback

from utils.webpage_text import TextPageHeading

from components.data import load_data
from components.tabs import standard_tab_layout

from utils.config_file import (
    URLS,
    ElementsIDs,
)

dash.register_page(__name__, path=URLS.QUESTIONNAIRE.value, order=5)

df = load_data()


def layout():
    return standard_tab_layout(
        page_heading=TextPageHeading.questionnaire.value, figures=[]
    )
