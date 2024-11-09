import plotly.graph_objects as go
import plotly.io as pio

from utils.config_file import CHART_LAYOUT

custom_colors = (
    "#277da1",
    "#577590",
    "#4d908e",
    "#43aa8b",
    "#90be6d",
    "#f9c74f",
    "#f9844a",
    "#f8961e",
    "#f3722c",
    "#f94144",
)


custom_template = pio.templates["ggplot2"].update(
    layout_colorway=custom_colors,
    layout_plot_bgcolor="rgba(0,0,0,0)",
    layout_paper_bgcolor="rgba(0,0,0,0)",
)

pio.templates[CHART_LAYOUT.template.value] = custom_template
