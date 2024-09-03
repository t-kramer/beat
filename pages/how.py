import dash

import dash_bootstrap_components as dbc
from dash import dcc
from dash import Dash, dcc, html, Input, Output, callback

from utils.config_file import (
    URLS,
    ElementsIDs,
)

from utils.webpage_text import TextPageHeading

from components.tabs import standard_tab_layout
from components.charts import sunburst_sensors
from components.data import load_data

dash.register_page(__name__, path=URLS.HOW.value, order=3)

df = load_data()


def layout():
    return standard_tab_layout(
        page_heading=TextPageHeading.how.value, figures=[sunburst_sensors(df)]
    )
