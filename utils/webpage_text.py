from enum import Enum

app_name = "BEAT: Building Experiment Assistance Tool"


class TextFooter(Enum):
    acknowledgment = "This application has been developed by the Center for the Built Environment and the Technical University of Munich."


class TextNavBar(Enum):
    home: str = "Home"
    about: str = "About"


class TextPageHeading(Enum):
    physiology: str = "Measurement locations & sensors."
    environment: str = "Environmental parameters."
    participant: str = "Participant information."
    protocol: str = "Common protocols."
    questionnaire: str = "Thermal comfort questionnaires & cognitive tests."


class TextHome(Enum):
    model_selection = "Select model:"
    functionality_selection = "Select functionality:"
    chart_selection = "Select chart:"


class TextInfo(Enum):
    selected_parameters: str = "Select physiological parameter(s)."


class FilterText(Enum):
    study_type = "Study Type."
    country = "Country."
    building_typology = "Building Typology."
    year = "Year."
    physiological_parameters = "Physiological Parameters."
    data_table = "List of filtered studies."


class ChartTitles(Enum):
    body_site_map = "Body Site Map."
    sunburst_sensors = "Physiological Sensors."
    box_no_participants = "Number of Participants."
    chart_pie_age = "Age Distribution."
    chart_violin_sex = "Sex Distribution."
    bar_environmental = "Recorded Environmental Parameters."
    bar_thermal_questionnaire = "Thermal Questionnaires ADD SCALES."
    parallel_questionnaire_scales = "Questionnaires & Scales."
    box_session_length = "Session Length."
    box_normalisation_length = "Normalisation Length."
    scatter_test_temps = "Tested Temperatures."
    heatmap_protocol = "Protocol Heatmap."
    heatmap_selection = "Selection Criteria Heatmap."
