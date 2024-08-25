import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.config_file import CHART_LAYOUT


def bar_year(df):

    df["exp-id"] = df["exp-id"].astype(str)
    unique_studies = df.drop_duplicates(subset=["exp-id"])
    year_counts = unique_studies["pub-year"].value_counts().sort_index().reset_index()
    year_counts.columns = ["pub-year", "count"]

    fig = px.bar(
        year_counts,
        x="pub-year",
        y="count",
        width=CHART_LAYOUT.width.value,
        height=CHART_LAYOUT.height.value,
        template=CHART_LAYOUT.template.value,
    )

    return fig


def map_country(df):

    df["exp-id"] = df["exp-id"].astype(str)
    unique_studies = df.drop_duplicates(subset=["exp-id"])
    country_counts = unique_studies["country"].value_counts().reset_index()
    country_counts.columns = ["country", "count"]

    fig = px.choropleth(
        country_counts,
        locations="country",
        locationmode="country names",
        color="count",
        width=CHART_LAYOUT.width.value,
        height=CHART_LAYOUT.height.value,
        hover_name="country",
    )

    return fig


def pie_building_type(df):

    function_counts = df["function"].value_counts().reset_index()
    function_counts.columns = ["function", "count"]

    fig = px.pie(
        function_counts,
        names="function",
        values="count",
        width=CHART_LAYOUT.width.value,
        height=CHART_LAYOUT.height.value,
        template=CHART_LAYOUT.template.value,
    )

    return fig


def body_site_map(df):

    #! This is dummy data for testing purposes
    testing_location_counts = pd.DataFrame(
        {
            "physio-body-site": [
                "Forehead",
                "Nose",
                "Cheek",
                "Neck",
                "Chest",
                "Back",
                "Upper arm",
                "Abdomen",
                "Lumbar",
                "Forearm",
                "Buttock",
                "Wrist",
                "Finger",
                "Thigh",
                "Shin",
                "Calf",
                "Ankle",
                "Foot",
                "Sole",
            ],
            "count": [
                10,
                15,
                7,
                20,
                5,
                8,
                12,
                14,
                9,
                11,
                6,
                13,
                4,
                16,
                3,
                18,
                2,
                17,
                1,
            ],
        }
    )

    location_coordinates = pd.DataFrame(
        {
            # Format:'physio-body-site':[x, y]
            "Forehead": [-147.5, 262.5],
            "Nose": [-147.5, 240],
            "Cheek": [-160, 225],
            "Neck": [28, 203],
            "Chest": [-147.5, 157.5],
            "Back": [28, 152.5],
            "Upper arm": [-195, 140],
            "Abdomen": [-147.5, 75],
            "Lumbar": [28, 85],
            "Forearm": [-195, 75],
            "Buttock": [45, 55],
            "Wrist": [-205, 45],
            "Finger": [-215, -5],
            "Thigh": [28, -22.5],
            "Shin": [-170, -110],
            "Calf": [12.5, -110],
            "Ankle": [17.5, -165],
            "Foot": [-150, -190],
            "Sole": [17.5, -190],
        }
    )

    location_coordinates = location_coordinates.transpose().rename(
        columns={0: "x-coordinate", 1: "y-coordinate"}
    )
    location_coordinates.reset_index(inplace=True)
    location_coordinates.rename(columns={"index": "physio-body-site"}, inplace=True)

    merged_df = pd.merge(
        location_coordinates, testing_location_counts, on="physio-body-site"
    )

    fig = go.Figure()

    fig.add_layout_image(
        dict(
            source="./assets/img/body-site-chart-background.png",
            xref="x",
            yref="y",
            x=10,
            y=10,
            sizex=800,
            sizey=640,
            xanchor="center",
            yanchor="middle",
            opacity=1.0,
            layer="below",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=merged_df["x-coordinate"],
            y=merged_df["y-coordinate"],
            mode="markers",
            marker=dict(size=merged_df["count"] * 2.5, color="#db1492", opacity=0.8),
            text=merged_df["count"],  # Add the counts to the hover text
            hoverinfo="text",
        )
    )

    fig.update_xaxes(showgrid=False, showticklabels=False, range=[-350, 350])

    fig.update_yaxes(showgrid=False, showticklabels=False, range=[-320, 320])

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=False, zeroline=False),
        width=800,
        height=640,
        margin=dict(l=10, r=10, t=10, b=10),
    )

    return fig


def bar_parameter(df):

    parameter_counts = df.groupby("physio-parameter")["exp-id"].nunique()
    total_experiments = df["exp-id"].nunique()

    parameter_counts = parameter_counts.reset_index(name="exp-id count")
    parameter_counts["exp-id percentage"] = (
        parameter_counts["exp-id count"] / total_experiments
    ) * 100
    parameter_counts_sorted = parameter_counts.sort_values(
        "exp-id percentage", ascending=True
    )

    fig = px.bar(
        parameter_counts_sorted,
        x="exp-id percentage",
        y="physio-parameter",
        labels={
            "physio-parameter": "Physiological Parameter [-]",
            "exp-id percentage": "Percentage of Studies",
        },
        orientation="h",
    )

    fig.update_layout(
        xaxis_title="Percentage of Studies [%]",
        yaxis_title="Physiological Parameter [-]",
        template="plotly_white",
    )

    return fig


def sunburst_sensors(df):

    data = df[
        ["physio-parameter", "physio-sensor-type", "physio-sensor-brand"]
    ].dropna()

    fig = px.sunburst(
        data,
        path=["physio-parameter", "physio-sensor-type", "physio-sensor-brand"],
        height=600,  # to make chart bigger than default
        template=CHART_LAYOUT.template.value,
    )

    return fig


def box_number_participants(df):

    df["exp-id"] = df["exp-id"].astype(str)
    unique_studies = df.drop_duplicates(subset=["exp-id"])

    fig = px.box(
        unique_studies,
        y="part-no-tot",
        width=0.75 * CHART_LAYOUT.width.value,
        height=CHART_LAYOUT.height.value,
        template=CHART_LAYOUT.template.value,
    )

    return fig


def pie_age(df):

    df["exp-id"] = df["exp-id"].astype(str)
    unique_studies = df.drop_duplicates(subset=["exp-id"])

    fig = px.pie(
        unique_studies,
        names="age-group",
        width=0.75 * CHART_LAYOUT.width.value,
        height=CHART_LAYOUT.height.value,
        template=CHART_LAYOUT.template.value,
    )

    fig.update_layout(
        showlegend=False,
    )

    return fig


def violin_sex(df):

    df["exp-id"] = df["exp-id"].astype(str)
    unique_studies = df.drop_duplicates(subset=["exp-id"])

    fig = px.violin(
        unique_studies,
        y="fem-total-ratio",
        # box=True,
        # points="all",
        width=0.75 * CHART_LAYOUT.width.value,
        height=CHART_LAYOUT.height.value,
        template=CHART_LAYOUT.template.value,
    )

    return fig
