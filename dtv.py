import streamlit as st
import streamlit_authenticator as stauth
import yaml

from data_visualization import schedule, content, daily

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

    with st.sidebar:
        authenticator.logout('Logout', 'main')
        st.write(f'Welcome *{name}*')
        st.header("Configuration")
        view_options = ("schedules", "content", "daily data")
        selected_api = st.selectbox(
            label="Choose your data visualization:",
            options=view_options,
        )

        demo = schedule if selected_api == "schedules" else content if selected_api == "content" else daily

    df = demo(st.session_state["name"])
    st.markdown("""---""")
    st.download_button(
        "Download :floppy_disk:",
        df.to_csv(index=False).encode('utf-8'),
        f"{selected_api}.csv",
        "text/csv",
        key='download-csv',
        type='primary'
    )



elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')
