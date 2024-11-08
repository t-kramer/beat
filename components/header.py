import dash_bootstrap_components as dbc
import dash

from dash import dcc, html

from utils.webpage_text import (
    app_name,
)


def cbe_header():
    return html.Header(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Img(
                                src="../assets/img/logo-no-text.png", alt="tool-logo"
                            )
                        ],
                        className="tool-header-logo",
                    ),
                    html.Div([html.A(app_name, href="/")], className="cbe-tool-title"),
                    html.Nav(
                        [
                            html.A("About", href="about.html"),
                            html.A("Documentation", href="#"),
                            html.A("Data", href="#"),
                        ],
                        className="cbe-header-nav",
                    ),
                ],
                className="cbe-header-content",
            )
        ]
    )
