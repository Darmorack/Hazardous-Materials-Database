import sqlite3
import streamlit as st
from streamlit import session_state as ss


def HomeNav():
    st.sidebar.page_link("streamlit_app.py", label="Home", icon='🏠')


def LoginNav():
    st.sidebar.page_link("pages/account.py", label="Account", icon='🔐')


def InsertNav():
    st.sidebar.page_link("pages/insert.py", label="Insert", icon='➕')


def DeleteNav():
    st.sidebar.page_link("pages/delete.py", label="Delete", icon='🗑️')


def UpdateNav():
    st.sidebar.page_link("pages/update.py", label="Update", icon='🔄️')


def RecordsNav():
    st.sidebar.page_link("pages/reports.py", label="Reports", icon='📃')


def PermissionsNav():
    st.sidebar.page_link("pages/permissions.py", label="Permissions", icon='🚹')


def MenuButtons():

    with st.sidebar:
        st.markdown(f"""
            <a href="/" style="color:black;text-decoration: none;">
                <div style="display:table;margin-top:-3.5rem;margin-left:0%;">
                    <span style= "color: white; font-size: 1em">&nbsp;⚠️  HazMat</span>
                    <span style="font-size: 0.8em; color: white">v0.1.0</span>
                    <br>
                </div>
            </a>
            <br>
                """, unsafe_allow_html=True)

    if 'authentication_status' not in ss:
        ss.authentication_status = False

    # Always show the home and login navigators.
    HomeNav()
    LoginNav()

    # Show the other page navigators depending on the users' role.
    if ss["authentication_status"]:

        # I connect to the SQLite database here rather than in the outer scope so as not to interfere with
        # Streamlit's finicky threading model....
        conn = sqlite3.connect('Hazardous Materials Database.db')
        cur = conn.cursor()

        cur.execute("SELECT role FROM Users WHERE username = ?", (ss["name"],))
        role = cur.fetchone()[0]

        # (1) Only the admin role can access the Delete, Insert, Update, Permissions pages.
        if role == 'admin':
            InsertNav()
            UpdateNav()
            DeleteNav()
            PermissionsNav()

        # (2) Managers have read/write access, but cannot change user permissions.
        if role == 'manager':
            InsertNav()
            UpdateNav()
            DeleteNav()

        # (3) users with user and admin roles have access to the Records page
        RecordsNav()

        # Close the connection
        conn.close()

