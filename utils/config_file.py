import platform
from enum import Enum
from pydantic import BaseModel


class PAGE_LAYOUT(Enum):
    default_container_width = "md"
    column_width_full = 12
    column_width_primary = 9
    column_width_secondary = 3
    column_width_grid = 4
    infocard_align = "top"


class DataKeys(Enum):
    SKIN_TEMPARATURE = "Skin temperature"
    HEART_RATE = "Heart rate"
    DOPAMINE = "Dopamine"
    SWEAT = "Sweat"
    BODY_TEMPERATURE = "Body temperature"
    BLOOD_PRESSURE = "Blood pressure"
    METABOLIC_RATE = "Metabolic rate"
    EEG = "EEG"
    OXYGEN_SATURATION = "Oxygen saturation"


class ElementsIDs(Enum):
    NAVBAR = "id-navbar"
    NAVBAR_COLLAPSE = "navbar-collapse"
    NAVBAR_TOGGLER = "navbar-toggle"
    NAVBAR_BURGER_BUTTON = "burger-button"
    NAVBAR_ID_HOME = "id-nav-home"
    NAVBAR_ID_SETTINGS = "id-nav-settings"
    NAVBAR_ID_ABOUT = "id-nav-about"
    MODEL_SELECTION = "id-model-selection"
    CHART_SELECTION = "id-chart-selection"
    CHART_CONTAINER = "chart-container"
    CHART_BAR_YEAR = "id-chart-bar-year"
    CHART_MAP_COUNTRY = "id-chart-choropleth-country"
    CHART_MAP_BODY = "id-chart-chart-body"
    CHART_PIE_BUILDING_TYPE = "id-chart-pie-building-type"
    CHART_SUNBURST = "id-chart-sunburst"
    CHART_BOX_NO_PARTICIPANTS = "id-chart-box-no-participants"
    CHART_PIE_AGE = "id-chart-pie-age"
    CHART_HISTOGRAM_SEX = "id-chart-histogram-sex"
    CHART_BAR_ENVIRONMENTAL = "id-chart-bar-environmental"
    CHART_BAR_THERMAL_QUESTIONNAIRE = "id-chart-bar-thermal-questionnaire"
    CHART_PARALLEL_QUESTIONNAIRE_SCALES = "id-chart-parallel-questionnaire-scales"
    CHART_BOX_SESSION_LENGTH = "id-chart-box-session-length"
    CHART_BOX_NORMALISATION_LENGTH = "id-chart-box-normalisation-length"
    CHART_SCATTER_TEST_TEMPS = "id-chart-scatter-test-temps"
    CHART_HEATMAP_PROTOCOL = "id-chart-heatmap-protocol"
    CHART_HEATMAP_SELECTION = "id-chart-heatmap-selection"
    CHECKLIST_INPUT = "checklist-input"
    FOOTER = "id-footer"
    LOADING_TYPE = "circle"
    URL = "url"


class LABELS(Enum):
    BY_YEAR: str = "By Year"
    BY_COUNTRY: str = "By Country"
    BY_BUILDING_TYPE: str = "By Building Type"


class Config(Enum):
    DEBUG: bool = "macOS" in platform.platform()


class URLS(Enum):
    HOME: str = "/"
    EXPERIMENT: str = "/experiment"
    PHYSIOLOGY: str = "/physiology"
    ENVIRONMENT: str = "/environment"
    PARTICIPANTS: str = "/participants"
    PROTOCOL: str = "/protocol"
    QUESTIONNAIRE: str = "/questionnaire"


class Stores(Enum):
    INPUT_DATA = "store_input_data"


class CHART_LAYOUT(Enum):
    width: int = 800
    height: int = 400
    template: str = "beat_theme"
