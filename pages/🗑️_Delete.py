import streamlit as st
import sqlite3
import helpers.sidebar

st.set_page_config(
    page_title="Hazardous Materials Database",
    page_icon="🗑️",
    layout="wide"
)

helpers.sidebar.show()


# @st.cache_resource
# def init_connection():
#     return sqlite3.connect('Hazardous Materials Database.db')
#
#
# conn = init_connection()

conn = sqlite3.connect('Hazardous Materials Database.db')
cur = conn.cursor()

table_options = ["Select an Option", "Item", "Action"]
table_choice = st.selectbox("Which table would you like to delete from?", table_options)

# TODO: LOCK USER CHOICE

if table_choice == "Item":
    with st.expander("Item Attributes"):
        item_id = st.text_input("Item ID")
    if st.button('Confirm', key='delete_action'):
        cur.execute("DELETE FROM Item WHERE ItemID = ?", (item_id,))
        conn.commit()
        st.write("Successfully deleted an item")

if table_choice == "Action":
    with st.expander("Action Attributes"):
        action_id = st.text_input("Action ID")
        item_id = st.text_input("Item ID")
    if st.button('Confirm', key='delete_action'):
        cur.execute("DELETE FROM Actions WHERE ActionID = ? AND ItemID = ?", (action_id, item_id))
        conn.commit()
        st.write("Successfully deleted an action")


