import sqlite3

import bcrypt
import streamlit as st
from streamlit import session_state as ss
from modules.nav import MenuButtons

st.set_page_config(
    page_title="Hazardous Materials Database",
    page_icon="🔐",
    layout="wide"
)

# Connect to the SQLite database
conn = sqlite3.connect('Hazardous Materials Database.db')
cur = conn.cursor()


def get_roles():
    """Gets user roles from the Users table in the database."""
    cur.execute("SELECT username, role FROM Users")
    return dict(cur.fetchall())


st.header('Login or Register')

login_tab, register_tab, change_details_tab = st.tabs(['Login', 'Register', 'Change Details'])

with login_tab:
    if not ss.get("authentication_status", False):
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button('Login'):
            cur.execute("SELECT password, role FROM Users WHERE username = ?", (username,))
            result = cur.fetchone()

            if result and bcrypt.checkpw(password.encode('utf-8'), result[0]):
                ss["authentication_status"] = True
                ss["name"] = username
                ss["role"] = result[1]
                st.experimental_rerun()
            else:
                ss["authentication_status"] = False
                st.error('Username/password is incorrect')
    else:
        st.write(f'Welcome *{ss["name"]}*')
        if st.button('Logout'):
            ss["authentication_status"] = None
            ss["name"] = None
            ss["role"] = None
            # Remove login_tab
            st.experimental_rerun()

if not ss.get("registered", False):
    with register_tab:
        if not ss.get("authentication_status", False):
            username = st.text_input("Username", key="register_username")
            name = st.text_input("Name", key="register_name")
            email = st.text_input("Email", key="register_email")
            password = st.text_input("Password", type="password", key="register_password")

            if st.button('Register'):
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                cur.execute("INSERT INTO Users (username, name, email, password, role) VALUES (?, ?, ?, ?, 'user')",
                            (username, name, email, hashed_password))
                conn.commit()
                st.success('User registered successfully')
                ss["registered"] = True
                # Remove register_tab
                st.experimental_rerun()

if ss.get("authentication_status", False):
    with change_details_tab:
        new_password = st.text_input("New Password", type="password", key="change_password")
        confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")

        if st.button('Submit Changes') and new_password == confirm_password:
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
            cur.execute("UPDATE Users SET password = ? WHERE username = ?",
                        (hashed_password, ss["name"]))
            conn.commit()
            st.success('Password updated successfully')
        else:
            st.error('Passwords do not match')

# Call this late because we show the page navigator depending on the user's role
MenuButtons()
