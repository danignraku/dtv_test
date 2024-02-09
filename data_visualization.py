import pandas as pd
from mitosheet.streamlit.v1 import spreadsheet

list_of_roles = {
    "User1": "A",
    "User2": "B",
    "admin": "admin",
    "User3": "C"
}


def schedule(role: str) -> pd.DataFrame:
    role = list_of_roles[role]
    CSV_URL = 'dtv_data.csv'
    df = pd.read_csv(CSV_URL, sep=";")
    if role != 'admin':
        df = df[df["ROLE"] == role].drop(columns=["ROLE"])
        df = df.reset_index()
    new_dfs, _ = spreadsheet(df)
    return df


def content(role: str) -> pd.DataFrame:
    role = list_of_roles[role]
    CSV_URL = 'dtv_data.csv'
    df = pd.read_csv(CSV_URL, sep=";")
    if role != 'admin':
        df = df[df["ROLE"] == role].drop(columns=["ROLE"])

        df = df.drop(columns=['CHANNEL_NAME']).groupby(['CONTENT_TITLE']).mean()
        df = df.reset_index()
    new_dfs, _ = spreadsheet(df)
    return df


def daily(role: str) -> pd.DataFrame:
    role = list_of_roles[role]
    CSV_URL = 'daily_data.csv'
    df = pd.read_csv(CSV_URL, sep=";")
    if role != 'admin':
        df = df[df["ROLE"] == role].drop(columns=["ROLE"])
        df = df.reset_index()
    new_dfs, _ = spreadsheet(df)
    return df
