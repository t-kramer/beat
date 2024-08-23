import platform
from enum import Enum
from pydantic import BaseModel


class Dimensions(Enum):
    default_container_width = "md"
    column_width_primary = 9
    column_width_secondary = 3


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
    CHART_PIE_BUILDING_TYPE = "id-chart-pie-building-type"
    CHECKLIST_INPUT = "checklist-input"
    URL = "url"
    FOOTER = "id-footer"


class LABELS(Enum):
    BY_YEAR: str = "By Year"
    BY_COUNTRY: str = "By Country"
    BY_BUILDING_TYPE: str = "By Building Type"


class Config(Enum):
    # DEBUG: bool = False
    DEBUG: bool = "macOS" in platform.platform()


class URLS(Enum):
    HOME: str = "/"
    ABOUT: str = "/about"
    WHAT: str = "/what"
    WHERE: str = "/where"
    HOW: str = "/how"
    WHO: str = "/who"


class Stores(Enum):
    INPUT_DATA = "store_input_data"


class CHART_LAYOUT(Enum):
    width: int = 800
    height: int = 400
    template: str = "plotly_white"
