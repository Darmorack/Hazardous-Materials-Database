import streamlit as st
from streamlit import session_state as ss
from modules.nav import MenuButtons
import sqlite3

st.set_page_config(
    page_title="Hazardous Materials Database",
    page_icon="➕",
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

st.title("Insert into the Database")

table_options = ["Select an Option", "Item", "Action"]
table_choice = st.selectbox("Which table would you like to insert into?", table_options)

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
        cur.execute(
            "INSERT OR IGNORE INTO Item ('ItemID', 'Item Name', 'Quantity', 'Category', 'Hazard/Hazard Tracking System "
            "References', 'Potential For Exposure', 'Controls/Mitigations', 'References', 'Notes') VALUES(?, ?, ?, ?, "
            "?, ?, ?, ?, ?)",
            (item_id, item_name, quantity, category, hazard_tracking_system_references, potential_for_exposure,
             controls_mitigations, references, notes)
        )
        cur.execute(
            "INSERT OR IGNORE INTO Subsystem (Name) VALUES (?)",
            (subsystem_name,)
        )
        cur.execute(
            "INSERT OR IGNORE INTO Contains ('SubsystemName', 'ItemID') VALUES (?, ?)",
            (subsystem_name, item_id)
        )
        cur.execute(
            "INSERT OR IGNORE INTO Restriction ('RestrictionType', 'Carcinogen Threshold', 'Non-Carcinogen Threshold') VALUES ("
            "?, ?, ?)",
            (restriction_name, carcinogen_threshold, non_carcinogen_threshold)
        )
        cur.execute(
            "INSERT OR IGNORE INTO Substance ('Name', 'CAS Numbers', 'Restriction', 'Carcinogenicity') VALUES (?, ?, ?, ?)",
            (substance_name, casnumbers, restriction_name, carcinogenicity)
        )
        cur.execute(
            "INSERT OR IGNORE INTO 'Hazardous Component' ('ItemID', 'SubstanceName', 'Weight Percentage') VALUES (?, ?, ?)",
            (item_id, substance_name, weight_percentage)
        )
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
        cur.execute(
            "INSERT OR IGNORE INTO Actions ('ActionID', 'Person', 'Status', 'Due Date', 'Completion Date', 'Notes', 'ItemID') "
            "VALUES(?, ?, ?, ?, ?, ?, ?)",
            (action_id, person, status, due_date, completion_date, notes, item_id)
        )
        conn.commit()
        st.write("Successfully inserted a new action")
