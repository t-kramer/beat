import pandas as pd
import plotly.express as px

import dash

import dash_bootstrap_components as dbc
from dash import dcc
from dash import dcc, html, Input, Output, State, callback


from utils.config_file import PAGE_LAYOUT, URLS, ElementsIDs, LABELS

from utils.webpage_text import TextInfo

dash.register_page(__name__, path=URLS.ENVIRONMENT.value, order=3)


def layout():
    return None
