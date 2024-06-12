import streamlit as st
import sqlite3


st.write("Hello, World!")


@st.cache_resource
def init_connection():
    return sqlite3.connect('hazmat.db')


conn = init_connection()

st.write('Database Connected!')

page = st.sidebar.selectbox('Page', ('Search', 'A', 'B', 'C'))
