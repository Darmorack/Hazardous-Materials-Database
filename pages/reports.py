import streamlit as st
from streamlit import session_state as ss
from modules.nav import MenuButtons
import sqlite3

st.set_page_config(
    page_title="Hazardous Materials Database",
    page_icon="📃",
    layout="wide"
)

# If the user reloads or refreshes the page while still logged in,
# go to the account page to restore the login status.
if 'authentication_status' not in ss:
    st.switch_page('./pages/account.py')

MenuButtons()
st.header('Generate a New Report')
st.write('This page is accessible by all users including the admins.')