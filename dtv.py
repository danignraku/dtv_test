import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from mitosheet.streamlit.v1 import spreadsheet

st.set_page_config(
    page_title="DTV Demo",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# Example of a DTV Demo!"
    }
)

from yaml.loader import SafeLoader

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
name, authentication_status, username = authenticator.login('main')
if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')

    CSV_URL = 'dtv_data.csv'
    df = pd.read_csv(CSV_URL, sep=";")
    if st.session_state["role"] != 'admin':
        df = df[df["role"] == st.session_state["role"]]
    new_dfs, _ = spreadsheet(df)
    st.write(new_dfs)
elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')
