import streamlit as st
from streamlit import session_state as ss
from modules.nav import MenuButtons
import sqlite3

st.set_page_config(
    page_title="Hazardous Materials Database",
    page_icon="🗑️",
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

st.title("Delete from the Database")

table_options = ["Select an Option", "Item", "Action"]
table_choice = st.selectbox("Which table would you like to delete from?", table_options)
cur.execute('SELECT ItemID FROM Item')
items = [item[0] for item in cur.fetchall()]
cur.execute('SELECT ActionID FROM Actions')
actions = [action[0] for action in cur.fetchall()]

if table_choice == "Item":
    item_id = st.selectbox("Select an item you want to delete", items)

    if st.button('Confirm', key='delete_action'):
        cur.execute("DELETE FROM Item WHERE ItemID = ?", (item_id,))
        conn.commit()
        st.write("Successfully deleted an item")

if table_choice == "Action":
    action_id = st.selectbox("Select an action you want to delete", actions)
    item_id = st.selectbox("Select an item you want to delete", items)
    if st.button('Confirm', key='delete_action'):
        cur.execute("DELETE FROM Actions WHERE ActionID = ? AND ItemID = ?", (action_id, item_id))
        conn.commit()
        st.write("Successfully deleted an action")