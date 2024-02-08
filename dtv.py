import streamlit as st
import streamlit_authenticator as stauth
from mitosheet.streamlit.v1 import spreadsheet
import yaml

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
    st.set_page_config(
        page_title="DTV Demo",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'About': "# Example of a DTV Demo!"
        }
    )

    CSV_URL = 'https://raw.githubusercontent.com/plotly/datasets/master/tesla-stock-price.csv'
    new_dfs, _ = spreadsheet(CSV_URL)

    st.write(new_dfs)
elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')
