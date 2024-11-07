from dash import dash_table
import pandas as pd


def data_table(df):

    data = df.drop_duplicates(subset=["exp-id"])[
        ["pub-year", "paper", "authors", "institutes", "country", "pub-name", "doi"]
    ]

    print(data.columns)
    return dash_table.DataTable(
        data.to_dict("records"),
        columns=[
            {
                "name": i,
                "id": i,
                "deletable": False,
                "editable": False,
                "selectable": True,
            }
            for i in data.columns
        ],
        fixed_rows={"headers": True},
        page_size=20,
        style_table={"overflowY": "auto", "height": "400px"},
        style_data={
            "whiteSpace": "nowrap",  # Prevent line breaks
            "height": "auto",
            "fontSize": "14px",  # Larger font size
            "fontFamily": "Open Sans",  # Use Helvetica font
        },
        style_cell={
            "minWidth": "100px",  # Minimum column width
            "maxWidth": "250px",  # Maximum column width
            "overflow": "hidden",
            "textOverflow": "ellipsis",
            "textAlign": "left",
        },
        style_header={
            "fontSize": "16px",  # Same font size as data cells
            "fontFamily": "Open Sans",  # Use Helvetica font
            "fontWeight": "bold",  # Bold headers
        },
        tooltip_data=[
            {
                column: {"value": str(value), "type": "markdown"}
                for column, value in row.items()
            }
            for row in data.to_dict("records")
        ],
        tooltip_duration=None,
        sort_action="native",
        filter_action="native",
        id="data-table",
    )
