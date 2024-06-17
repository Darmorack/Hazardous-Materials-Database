import streamlit as st
import sqlite3
import helpers.sidebar

st.set_page_config(
    page_title="Hazardous Materials Database",
    page_icon="🔄",
    layout="wide"
)

helpers.sidebar.show()


conn = sqlite3.connect('Hazardous Materials Database.db')
cur = conn.cursor()

table_options = ["Select an Option", "Item", "Action"]
table_choice = st.selectbox("Which table would you like to update?", table_options)

