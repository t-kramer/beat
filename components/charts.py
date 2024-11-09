import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.config_file import CHART_LAYOUT


def get_unique_studies(df):
    df["exp-id"] = df["exp-id"].astype(str)
    unique_studies = df.drop_duplicates(subset=["exp-id"])
    return unique_studies


def bar_year(df):

    unique_studies = get_unique_studies(df)
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

    fig.update_layout(
        xaxis_title="Publication Year [a]",
        yaxis_title="Number of Studies [-]",
        xaxis=dict(tickmode="linear"),
    )

    return fig


def map_country(df):

    unique_studies = get_unique_studies(df)
    country_counts = unique_studies["country"].value_counts().reset_index()
    country_counts.columns = ["country", "count"]

    fig = go.Figure(
        data=go.Choropleth(
            locations=country_counts["country"],
            locationmode="country names",
            z=country_counts["count"],
            text=country_counts["country"],
            marker_line_color="darkgray",
            marker_line_width=0.5,
            colorbar_title="Studies per Country [-]",
            colorscale="Viridis",
        )
    )

    fig.update_layout(
        geo=dict(
            showframe=False, showcoastlines=False, projection_type="equirectangular"
        ),
        width=CHART_LAYOUT.width.value,
        height=CHART_LAYOUT.height.value,
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
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

    body_site_counts = df["physio-body-site"].value_counts().reset_index()
    body_site_counts.columns = ["physio-body-site", "count"]

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

    merged_df = pd.merge(location_coordinates, body_site_counts, on="physio-body-site")

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
            marker=dict(size=merged_df["count"] * 1, color="#db1492", opacity=0.8),
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

    data = (
        df[["exp-id", "physio-parameter", "physio-sensor-type", "physio-sensor-brand"]]
        .dropna()
        .drop_duplicates(subset=["exp-id", "physio-parameter"])
    )

    fig = px.sunburst(
        data,
        path=["physio-parameter", "physio-sensor-type", "physio-sensor-brand"],
        height=600,  # to make chart bigger than default
        template=CHART_LAYOUT.template.value,
    )

    return fig


def box_number_participants(df):

    unique_studies = get_unique_studies(df)

    fig = px.box(
        unique_studies,
        y="part-no-tot",
        width=CHART_LAYOUT.width.value,
        height=CHART_LAYOUT.height.value,
        template=CHART_LAYOUT.template.value,
    )

    fig.update_layout(
        yaxis_title="No. Subjects [-]",
    )

    return fig


def pie_age(df):

    unique_studies = get_unique_studies(df)

    fig = px.pie(
        unique_studies,
        names="age-group",
        width=CHART_LAYOUT.width.value,
        height=CHART_LAYOUT.height.value,
        template=CHART_LAYOUT.template.value,
    )

    return fig


def histogram_sex(df):

    unique_studies = get_unique_studies(df)

    unique_values = unique_studies["fem-total-ratio"].dropna()
    sorted_values = sorted(unique_values)

    category_orders = {"fem-total-ratio": sorted_values}

    fig = px.histogram(
        unique_studies,
        x="fem-total-ratio",
        # points="all",
        width=CHART_LAYOUT.width.value,
        height=CHART_LAYOUT.height.value,
        template=CHART_LAYOUT.template.value,
        category_orders=category_orders,
    )

    fig.update_layout(
        yaxis_title="No. Studies [-]",
        xaxis_title="Female-Total Ratio [-]",
    )

    return fig


def hor_bar_environmental_parameters(df):

    unique_studies = get_unique_studies(df)

    env_columns = [col for col in unique_studies.columns if col.startswith("env-")]
    env_df = unique_studies[env_columns]

    env_coverage = env_df.notna().mean() * 100
    env_coverage_df = env_coverage.reset_index()
    env_coverage_df.columns = ["environment_parameter", "coverage_percentage"]

    env_coverage_df = env_coverage_df.sort_values(
        "coverage_percentage", ascending=False
    )

    fig = px.bar(
        env_coverage_df,
        y="coverage_percentage",
        x="environment_parameter",
        labels={
            "coverage_percentage": "Coverage Percentage [%]",
            "environment_parameter": "Environmental Parameter",
        },
        width=CHART_LAYOUT.width.value,
        height=CHART_LAYOUT.height.value,
        template=CHART_LAYOUT.template.value,
    )

    return fig


def bar_thermal_questionnaires(df):

    unique_studies = get_unique_studies(df)

    exploded_df = unique_studies.assign(
        thermal_questionnaire_split=unique_studies["feedback-quest-type"].str.split(
            ", "
        )
    ).explode("thermal_questionnaire_split")

    df = exploded_df["thermal_questionnaire_split"].value_counts().reset_index()
    df.columns = ["thermal_questionnaire_split", "count"]
    # df["environment_parameter_percentage"] = (df["count"] / len(unique_studies)) * 100

    df = df.sort_values("count", ascending=False)

    fig = px.bar(
        df,
        y="count",
        x="thermal_questionnaire_split",
        labels={
            "count": "No. of Studies [-]",
            "thermal_questionnaire_split": "Thermal Questionnaire [-]",
        },
        width=CHART_LAYOUT.width.value,
        height=CHART_LAYOUT.height.value,
        template=CHART_LAYOUT.template.value,
    )

    return fig


def parallel__questionnaires_scales(df):

    unique_studies = get_unique_studies(df)

    exploded_df = unique_studies.assign(
        thermal_questionnaire_split=unique_studies["feedback-quest-type"].str.split(
            ", "
        )
    ).explode("thermal_questionnaire_split")

    df = exploded_df["thermal_questionnaire_split"].value_counts().reset_index()

    fig = px.parallel_categories(
        exploded_df,
        dimensions=["thermal_questionnaire_split", "feedback-scales"],
        labels={
            "feedback-scales": "Question Scaling [-]",
            "thermal_questionnaire_split": "Thermal Questionnaire [-]",
        },
        width=CHART_LAYOUT.width.value,
        height=CHART_LAYOUT.height.value,
        template=CHART_LAYOUT.template.value,
    )

    return fig


def box_session_length(df):

    df = get_unique_studies(df)

    # ! get rid of multiple values in session length
    # ? convert to numeric
    df["session-length"] = pd.to_numeric(df["session-length"], errors="coerce")

    fig = px.box(
        df,
        y="session-length",
        labels={
            "session-length": "Session length [min]",
        },
        width=CHART_LAYOUT.width.value,
        height=CHART_LAYOUT.height.value,
        template=CHART_LAYOUT.template.value,
    )

    return fig


def box_normalisation_length(df):

    df = get_unique_studies(df)

    fig = px.box(
        df,
        y="normalisation-length",
        labels={
            "normalisation-length": "Normalisation length [min]",
        },
        width=CHART_LAYOUT.width.value,
        height=CHART_LAYOUT.height.value,
        template=CHART_LAYOUT.template.value,
    )

    return fig


def scatter_test_temp(df):

    df = get_unique_studies(df)

    df = df.dropna(subset=["part-no-tot"])

    fig = px.scatter(
        df,
        x="tested-t-min",
        y="tested-t-max",
        color="physio-parameter",
        size="part-no-tot",  # ? replace with something else
        labels={
            "tested-t-min": "Min. Tested Temperature [°C]",
            "tested-t-max": "Max. Tested Temperature [°C]",
            "physio-parameter": "Physiological Parameter [-]",
        },
        width=CHART_LAYOUT.width.value,
        height=CHART_LAYOUT.height.value,
        template=CHART_LAYOUT.template.value,
    )

    return fig


def heatmap_protocol(df):

    df = get_unique_studies(df)

    df = df.fillna(0)
    df.set_index("exp-id", inplace=True)

    protocol_columns = df.filter(like="protocol-")
    protocol_columns = protocol_columns.transpose()

    fig = px.imshow(
        protocol_columns,
        labels=dict(x="Study ID", y="Criteria", color="Fulfilled"),
        x=protocol_columns.columns,
        y=protocol_columns.index,
        aspect=0.5,
        color_continuous_scale=["White", "SlateBlue"],  # Colors for 0 and 1
        width=CHART_LAYOUT.width.value,
        height=CHART_LAYOUT.height.value,
        template=CHART_LAYOUT.template.value,
    )

    fig.update_coloraxes(
        colorbar=dict(
            tickvals=[0, 1],
            ticktext=["False", "True"],
        )
    )

    fig.update_layout(
        xaxis_title="Study ID",
        yaxis_title="Item",
        xaxis=dict(tickmode="linear", showticklabels=False, ticks=""),
        yaxis=dict(tickmode="linear"),
    )

    return fig


def heatmap_selection(df):

    df = get_unique_studies(df)

    df = df.fillna(0)
    df.set_index("exp-id", inplace=True)

    protocol_columns = df.filter(like="select-")
    protocol_columns = protocol_columns.transpose()

    fig = px.imshow(
        protocol_columns,
        labels=dict(x="Study ID", y="Criteria", color="Fulfilled"),
        x=protocol_columns.columns,
        y=protocol_columns.index,
        aspect=0.5,
        color_continuous_scale=["White", "MediumVioletRed"],  # Colors for 0 and 1
        width=CHART_LAYOUT.width.value,
        height=CHART_LAYOUT.height.value,
        template=CHART_LAYOUT.template.value,
    )

    fig.update_coloraxes(
        colorbar=dict(
            tickvals=[0, 1],
            ticktext=["False", "True"],
        )
    )

    fig.update_layout(
        xaxis_title="Study ID [-]",
        yaxis_title="Selection Criteria [-]",
        xaxis=dict(tickmode="linear", showticklabels=False, ticks=""),
        yaxis=dict(tickmode="linear"),
    )

    return fig
