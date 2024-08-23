import dash_bootstrap_components as dbc


def standard_dropdown():
    return dbc.Select(
        options=[
            {"label": "Skin temperature", "value": "Skin Temperature"},
            {"label": "Heart Rate", "value": "Heart Rate"},
            {"label": "Dopamine", "value": "Dopamine"},
            {"label": "Sweat", "value": "Sweat"},
            {"label": "Body Temperature", "value": "Body Temperature"},
        ],
    )


def parameter_checklist():
    return dbc.Checklist(
        id="parameter_checklist",
        options=[
            {"label": "Skin temperature", "value": "Skin Temperature"},
            {"label": "Heart Rate", "value": "Heart Rate"},
            {"label": "Dopamine", "value": "Dopamine"},
            {"label": "Sweat", "value": "Sweat"},
            {"label": "Body Temperature", "value": "Body Temperature"},
        ],
        value=[
            "Skin Temperature",
            "Heart Rate",
            "Dopamine",
            "Sweat",
            "Body Temperature",
        ],
        switch=True,
    )
