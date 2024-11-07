import dash_bootstrap_components as dbc
from dash import dcc

from utils.config_file import DataKeys


def standard_dropdown():
    return dbc.Select(
        options=[
            {"label": "Skin Temperature", "value": "Skin Temperature"},
            {"label": "Heart Rate", "value": "Heart Rate"},
            {"label": "Dopamine", "value": "Dopamine"},
            {"label": "Sweat", "value": "Sweat"},
            {"label": "Body Temperature", "value": "Body Temperature"},
        ],
    )


def parameter_checklist():
    return dbc.Checklist(
        id="parameter-checklist",
        options=[
            {"label": "Skin Temperature", "value": DataKeys.SKIN_TEMPARATURE.value},
            {"label": "Heart Rate", "value": DataKeys.HEART_RATE.value},
            {"label": "Dopamine", "value": DataKeys.DOPAMINE.value},
            {"label": "Sweat", "value": DataKeys.SWEAT.value},
            {"label": "Body Temperature", "value": DataKeys.BODY_TEMPERATURE.value},
            {"label": "Blood Pressure", "value": DataKeys.BLOOD_PRESSURE.value},
            {"label": "Metabolic Rate", "value": DataKeys.METABOLIC_RATE.value},
            {"label": "EEG", "value": DataKeys.EEG.value},
            {"label": "Oxygen Saturation", "value": DataKeys.OXYGEN_SATURATION.value},
        ],
        value=[
            DataKeys.SKIN_TEMPARATURE.value,
            DataKeys.HEART_RATE.value,
            DataKeys.DOPAMINE.value,
            DataKeys.SWEAT.value,
            DataKeys.BODY_TEMPERATURE.value,
            DataKeys.BLOOD_PRESSURE.value,
            DataKeys.METABOLIC_RATE.value,
            DataKeys.EEG.value,
            DataKeys.OXYGEN_SATURATION.value,
        ],
        switch=True,
    )


def study_type_checklist():
    return dbc.Checklist(
        id="study-type-checklist",
    )


def country_dropdown():
    return dcc.Dropdown(
        id="country-dropdown",
        placeholder="Select Country",
        multi=True,
    )


def building_typology_checklist():
    return dbc.Checklist(
        id="building-typology-checklist",
        inline=True,
    )


# def year_slider():
#     return dcc.RangeSlider(
#         id="year-slider",
#         step=1,
#         marks={},
#     )


def year_slider(min_year, max_year):
    # Set initial value to cover the full range of years
    initial_value = [min_year, max_year]

    # Generate marks for every year in the range
    marks = {str(year): str(year) for year in range(min_year, max_year + 1)}

    return dcc.RangeSlider(
        id="year-slider",
        min=min_year,
        max=max_year,
        step=1,
        marks=marks,
        value=initial_value,  # Start with the full range selected
    )
