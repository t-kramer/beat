from enum import Enum

app_name = "BEAT: Building Experiment Assistance Tool"


class TextFooter(Enum):
    acknowledgment = "This application has been developed by the Center for the Built Environment and the Technical University of Munich."


class TextNavBar(Enum):
    home: str = "Home"
    about: str = "About"


class TextHome(Enum):
    model_selection = "Select model:"
    functionality_selection = "Select functionality:"
    chart_selection = "Select chart:"