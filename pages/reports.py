import streamlit as st
from streamlit import session_state as ss
from modules.nav import MenuButtons
import sqlite3
import pandas as pd

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

# Connect to the database.
conn = sqlite3.connect('Hazardous Materials Database.db')
cur = conn.cursor()

table_options = ["Select an Option", "Items & Components Report", "Full Report", "Items & Hazards|HTS References Report", "Item-Action Report"]
table_choice = st.selectbox("Which report would you like?", table_options)

if table_choice == "Items & Components Report":
    report = cur.execute("SELECT * FROM HazMatReport").fetchall()
    col_names = [description[0] for description in cur.description]
    df = pd.DataFrame(report, columns = col_names)
    st.dataframe(df)
    st.write("Success!")

if table_choice == "Full Report":
    report = cur.execute("SELECT * FROM FullReport").fetchall()
    col_names = [description[0] for description in cur.description]
    df = pd.DataFrame(report, columns = col_names)
    st.dataframe(df)
    st.write("Success!")

if table_choice == "Items & Hazards|HTS References Report":
    report = cur.execute("SELECT * FROM HazardReport").fetchall()
    col_names = [description[0] for description in cur.description]
    df = pd.DataFrame(report, columns = col_names)
    st.dataframe(df)
    st.write("Success!")

if table_choice == "Item-Action Report":
    st.write("Search for an Item:")
    item_id = st.text_input("Item ID")
    if st.button('Search', key='item_action_search'):
        report = cur.execute("SELECT * FROM ActionReport WHERE ItemID = ?", (item_id,)).fetchall()
        col_names = [description[0] for description in cur.description]
        df = pd.DataFrame(report, columns = col_names)
        st.dataframe(df)
        st.write("Success!")
