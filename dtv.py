import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet

#st.set_page_config(layout="wide")
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
#st.code(code)