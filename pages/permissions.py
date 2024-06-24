import sqlite3

import streamlit as st
from streamlit import session_state as ss
from modules.nav import MenuButtons

st.set_page_config(
    page_title="Hazardous Materials Database",
    page_icon="🚹",
    layout="wide"
)

# Connect to the SQLite database
conn = sqlite3.connect('Hazardous Materials Database.db')
cur = conn.cursor()

st.title('Manage User Permissions')
st.write('Note: Users should be given minimal permissions to prevent unauthorized access to the database.')

MenuButtons()

# Retrieve all users from the database
cur.execute("SELECT username FROM Users")
users = [user[0] for user in cur.fetchall()]

# Define the available roles
roles = ['admin', 'manager', 'user']

selected_user = st.selectbox('Select a user', users)
selected_role = st.selectbox('Select a role', roles)

# Create a button to update the user's role
if st.button('Update Role'):
    if selected_user == ss["name"]:
        st.error("You cannot change your own role.")
    else:
        cur.execute("UPDATE Users SET role = ? WHERE username = ?", (selected_role, selected_user))
        conn.commit()
        st.success(f"Updated {selected_user}'s role to {selected_role}")

# Close the connection
conn.close()

