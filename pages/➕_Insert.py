import streamlit as st
import sqlite3
import helpers.sidebar

st.set_page_config(
    page_title="Hazardous Materials Database",
    page_icon="➕",
    layout="wide"
)

helpers.sidebar.show()


@st.cache_resource
def init_connection():
    return sqlite3.connect('Hazardous Materials Database.db')


conn = init_connection()

table_options = ["Select an Option", "Item", "Action"]
table_choice = st.selectbox("Which table would you like to insert into?", table_options)
