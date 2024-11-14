import dash_bootstrap_components as dbc
import dash

from dash import dcc, html


def cbe_footer():
    return html.Footer(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.Img(
                                src="../assets/img/CBE-logo-2019-white.png",
                                alt="CBE Logo",
                            ),
                            html.Img(src="../assets/img/tum.png", alt="TUM Logo"),
                        ],
                        className="cbe-footer-logo",
                    ),
                    html.Nav(
                        [
                            html.A(
                                "Contact Us",
                                href="https://cbe.berkeley.edu/about-us/contact/",
                                target="_blank",
                            ),
                            html.A(
                                "Report Issues",
                                href="https://github.com/CenterForTheBuiltEnvironment/cbe-tool-template/issues/new?labels=bug&template=issue--bug-report.md",
                                target="_blank",
                            ),
                        ],
                        className="cbe-footer-links",
                    ),
                    html.Nav(
                        [
                            html.A(
                                html.Img(
                                    src="../assets/img/github-white-transparent.png",
                                    alt="GitHub",
                                ),
                                href="#",
                            ),
                            html.A(
                                html.Img(
                                    src="../assets/img/linkedin-white.png",
                                    alt="LinkedIn",
                                ),
                                href="#",
                            ),
                        ],
                        className="cbe-social-links",
                    ),
                    html.Div(
                        [
                            html.B("Please cite us if you use this software:"),
                            html.Div(
                                [
                                    "Kramer, T., Kobas, B., 2024. BEAT: A Building Experiment Assistant Tool. SoftwareX 12, 100563.",
                                    html.A(
                                        "https://doi.org/10.1016/j.softx.2020.100563",
                                        href="https://doi.org/10.1016/j.softx.2020.100563",
                                        target="_blank",
                                        className="cbe-doi-link",
                                    ),
                                ]
                            ),
                        ],
                        className="cbe-citation-info",
                    ),
                ],
                className="cbe-footer-content",
            ),
            html.Div(
                [
                    html.Div(
                        "Copyright © 2024 The Center for the Built Environment and UC Regents. All rights reserved."
                    ),
                    html.Div(
                        [
                            html.Div("Version 1.00"),
                            html.A(
                                html.Img(
                                    src="https://img.shields.io/badge/License-MIT-yellow.svg",
                                    alt="License: MIT",
                                ),
                                href="https://opensource.org/licenses/MIT",
                                className="mit-license-badge",
                            ),
                        ],
                        className="cbe-version-license",
                    ),
                ],
                className="cbe-footnotes",
            ),
        ]
    )
