import streamlit as st
import sqlite3
import helpers.sidebar

st.set_page_config(
    page_title="Hazardous Materials Database",
    page_icon="➕",
    layout="wide"
)

helpers.sidebar.show()

conn = sqlite3.connect('Hazardous Materials Database.db')
cur = conn.cursor()

table_options = ["Select an Option", "Item", "Action"]
table_choice = st.selectbox("Which table would you like to insert into?", table_options)

# TODO: LOCK USER CHOICE
if table_choice == "Item":
    with st.expander("Item Attributes"):
        item_id = st.text_input("Enter Item's ID")
        item_name = st.text_input("Enter Item's Name")
        references = st.text_input("Enter References")
        potential_for_exposure = st.text_input("Enter Potential for Exposure")
        controls_mitigations = st.text_input("Enter Controls/Mitigations")
        hazard_tracking_system_references = st.text_input("Enter Hazard/Hazard Tracking System References")
        notes = st.text_input("Enter Notes")
        quantity = st.text_input("Quantity")
        category = st.text_input("Enter Category")

    with st.expander("Subsystem Attributes"):
        subsystem_name = st.text_input("Subsystem Name")

    with st.expander("Hazardous Component(s)"):
        substance_name = st.text_input("Substance Name")
        casnumbers = st.text_input("CAS Numbers")
        carcinogenicity = st.text_input("Carcinogenicity")
        weight_percentage = st.text_input("Weight Percentage")
        restriction_name = st.text_input("Restriction Name")
        carcinogen_threshold = st.text_input("Carcinogen Threshold")
        non_carcinogen_threshold = st.text_input("Non-Carcinogen Threshold")

    if st.button('Insert Item', key='submit_item'):
        # TODO SQL query here
        conn.commit()
        st.write("Successfully inserted a new item")

if table_choice == "Action":
    with st.expander("Action Attributes"):
        action_id = st.text_input("Action ID")
        item_id = st.text_input("Item ID")
        person = st.text_input("Person")
        due_date = st.text_input("Due Date")
        status = st.text_input("Status")
        completion_date = st.text_input("Completion Date")
        notes = st.text_input("Notes")

    if st.button('Insert Action', key='submit_action'):
        # TODO SQL query here
        conn.commit()
        st.write("Successfully inserted a new action")

