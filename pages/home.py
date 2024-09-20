import dash
from dash import html
import dash_bootstrap_components as dbc

from utils.config_file import (
    URLS,
    ElementsIDs,
)

dash.register_page(__name__, path=URLS.HOME.value, order=0)


def layout():
    return dbc.Container(
        html.Div(
            "This is going to provide a manual for the user to use the application and will show a summary of the entire data set."
        )
    )
