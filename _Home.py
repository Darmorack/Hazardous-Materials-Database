import streamlit as st
import sqlite3
import helpers.sidebar

st.set_page_config(
    page_title="Hazardous Materials Database",
    page_icon="🏠",
    layout="wide"
)

helpers.sidebar.show()

# st.toast("Welcome!", icon="⚠️")
st.write("Welcome to the Hazardous Materials Database!")
st.write("I will add the home emoji to this file's name later. My windows terminal doesn't like it.")

# Run the app by starting/activating a venv, then running: streamlit run _Home.py in your IDE's terminal
