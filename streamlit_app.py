import streamlit as st
from streamlit import session_state as ss
from modules.nav import MenuButtons

st.set_page_config(
    page_title="Hazardous Materials Database",
    page_icon="🏠",
    layout="wide"
)

# If the user reloads or refreshes the page while still logged in,
# go to the account page to restore the login status.
if 'authentication_status' not in ss:
    st.switch_page('./pages/account.py')


MenuButtons()
st.header('Home')


# Protected content in home page.
if ss.authentication_status:
    st.write('⚠️ Welcome to the Hazardous Materials Database!  ⚠️')
else:
    st.write('Please log in on login page.')
