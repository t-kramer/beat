import pandas as pd


def get_unique_studies(df):
    df["exp-id"] = df["exp-id"].astype(str)
    unique_studies = df.drop_duplicates(subset=["exp-id"])
    return unique_studies
