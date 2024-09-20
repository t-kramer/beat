from enum import Enum

app_name = "BEAT: Building Experiment Assistance Tool"


class TextFooter(Enum):
    acknowledgment = "This application has been developed by the Center for the Built Environment and the Technical University of Munich."


class TextNavBar(Enum):
    home: str = "Home"
    about: str = "About"


class TextPageHeading(Enum):
    measurement: str = "Measurement locations & sensors."
    participant: str = "Participant information."
    protocol: str = "Common protocols."
    questionnaire: str = "Thermal comfort questionnaires & cognitive tests."


class TextHome(Enum):
    model_selection = "Select model:"
    functionality_selection = "Select functionality:"
    chart_selection = "Select chart:"


class TextInfo(Enum):
    selected_parameters: str = "Select physiological parameter(s)."


class ChartTitles(Enum):
    body_site_map = "Body Site Map"
    sunburst_sensors = "Physiological Sensors"
    box_no_participants = "Number of Participants"
    chart_pie_age = "Age Distribution"
    chart_violin_sex = "Sex Distribution"
    bar_environmental = "Recorded Environmental Parameters"
    bar_thermal_questionnaire = "Thermal Questionnaires ADD SCALES"
    box_session_length = "Session Length ADD NORMALISATION"
