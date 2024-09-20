import dash_bootstrap_components as dbc

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
        id="parameter_checklist",
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
