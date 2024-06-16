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

if table_choice == "Item":
    item_id = st.text_input("Enter Item's ID")
    references = st.text_input("Enter References")
    potential_for_exposure = st.text_input("Enter Potential for Exposure")
    controls_mitigations = st.text_input("Enter Controls/Mitigations")
    hazard_tracking_system_references = st.text_input("Enter Hazard/Hazard Tracking System References")
    notes = st.text_input("Enter Notes")
    quantity = st.text_input("Enter Quantity")
    category = st.text_input("Enter Category")
