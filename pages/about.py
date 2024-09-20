import dash
from dash import html
import dash_bootstrap_components as dbc

from utils.config_file import (
    URLS,
    ElementsIDs,
)


def create_section(title, content):
    return dbc.Col(
        children=[
            html.H6(title, style={"font-weight": "bold"}),
            html.P(content),
        ],
        width=6,
    )


def layout():
    return dbc.Container(
        children=[
            dbc.Row(
                dbc.Placeholder(
                    xs=6,
                    size="lg",
                    animation="wave",
                ),
                justify="center",
            ),
            dbc.Row(
                create_section(
                    "What is BEAT.",
                    "BEAT is a database of academic publications in the field of thermal comfort, based on physiological data. At its current version, it only includes metadata from the experiments, ...",
                )
            ),
            dbc.Row(
                create_section(
                    "Why BEAT.",
                    "The field of thermal comfort is a very active field of research, with new publications coming out every year. However, the field is very fragmented, with many different experiments, ...",
                )
            ),
            dbc.Row(
                create_section(
                    "How to use BEAT.",
                    "You can use BEAT to search for publications that are relevant to your research. You can search by author, publication year, ...",
                )
            ),
            dbc.Row(
                create_section(
                    "Where does BEAT get its data.",
                    "BEAT gets its data from the ASHRAE database, which is a collection of academic publications in the field of thermal comfort. BEAT only includes publications that have physiological data, ...",
                )
            ),
        ],
    )
