import streamlit as st
from streamlit import session_state as ss
from modules.nav import MenuButtons
import sqlite3

st.set_page_config(
    page_title="Hazardous Materials Database",
    page_icon="🔄",
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

st.title("Update the Database")

table_options = ["Select an Option", "Item", "Action", "Substance", "Restriction"]
table_choice = st.selectbox("Which table would you like to update?", table_options)

if table_choice == "Action":
    with st.expander("Search for an Action"):
        action_id = st.text_input("Action ID")
        item_id = st.text_input("Item ID")
        if st.button('Search', key='action_search'):
            st.session_state['completion_date'], st.session_state['notes'], st.session_state['status'], \
                st.session_state['person'] = cur.execute(
                'SELECT "Completion Date",  "Notes", "Status", "Person" FROM Actions where ActionID = ? AND ItemID = ?',
                (action_id, item_id)).fetchone()
            st.write("Success!")

    with st.form(key='my_form'):
        with st.expander("Action Attributes"):
            completion_date = st.text_input("Completion Date", value=st.session_state.get('completion_date', ''),
                                            key='completion_date')
            notes = st.text_input("Notes", value=st.session_state.get('notes', ''), key='notes')
            status = st.text_input("Status", value=st.session_state.get('status', ''), key='status')
            person = st.text_input("Person", value=st.session_state.get('person', ''), key='person')
        if st.form_submit_button('Update Action'):
            cur.execute(
                "UPDATE Actions SET 'Completion Date' = ?, 'Notes' = ?, 'Status' = ?, 'Person' = ? WHERE ActionID = ? "
                "AND ItemID = ?", (completion_date, notes, status, person, action_id, item_id))
            conn.commit()
            st.write("Success!")

if table_choice == "Item":
    with st.expander("Search for an Item"):
        item_id = st.text_input("Item ID")
        if st.button('Search', key='item_search'):
            st.session_state['notes'], st.session_state['controls_mitigations'], st.session_state[
                'quantity'] = cur.execute(
                'SELECT "Notes", "Controls/Mitigations", "Quantity" FROM Item WHERE ItemID = ?', (item_id,)).fetchone()
            st.write("Success!")

    with st.form(key='item_form'):
        with st.expander("Item Attributes"):
            controls_mitigations = st.text_input("Enter Controls/Mitigations",
                                                 value=st.session_state.get('controls_mitigations', ''),
                                                 key='controls_mitigations')
            notes = st.text_input("Enter Notes", value=st.session_state.get('notes', ''), key='notes')
            quantity = st.number_input("Quantity", value=float(st.session_state.get('quantity', 0)), key='quantity',
                                       step=1.0)
        if st.form_submit_button('Update Item'):
            cur.execute("UPDATE Item SET 'Notes' = ?, 'Controls/Mitigations' = ?, 'Quantity' = ? WHERE ItemID = ?",
                        (notes, controls_mitigations, quantity, item_id))
            conn.commit()
            st.write("Success!")

if table_choice == "Substance":
    with st.expander("Search for a Substance"):
        substance_name = st.text_input("Substance Name")
        if st.button('Search', key='substance_search'):
            st.session_state['restriction_name'], st.session_state['cas_numbers'] = cur.execute(
                'SELECT "Restriction","CAS Numbers" FROM Substance WHERE Name = ?', (substance_name,)).fetchone()
            st.write("Success!")

    with st.form(key='substance_form'):
        with st.expander("Substance Attributes"):
            cas_numbers = st.text_input("CAS Numbers", value=st.session_state.get('cas_numbers', ''), key='cas_numbers')
            restriction_name = st.text_input("Restriction", value=st.session_state.get('restriction_name', ''),
                                             key='restriction_name')
        if st.form_submit_button('Update Substance'):
            cur.execute("Update Substance SET 'Restriction' = ?, 'CAS Numbers' = ? WHERE Name = ?",
                        (restriction_name, cas_numbers, substance_name))
            conn.commit()
            st.write("Success!")

if table_choice == "Restriction":
    with st.expander("Search for a Restriction"):
        restriction_type = st.text_input("Restriction Type")
        if st.button('Search', key='restriction_search'):
            st.session_state['carcinogen_threshold'], st.session_state['non_carcinogen_threshold'] = cur.execute(
                'SELECT "Carcinogen Threshold",  "Non-Carcinogen Threshold" FROM Restriction WHERE RestrictionType = ?',
                (restriction_type,)).fetchone()
            st.write("Success!")

    with st.form(key='restriction_form'):
        with st.expander("Restriction Attributes"):
            carcinogen_threshold = st.text_input("Carcinogen Threshold",
                                                 value=st.session_state.get('carcinogen_threshold', ''),
                                                 key='carcinogen_threshold')
            non_carcinogen_threshold = st.text_input("Non-Carcinogen Threshold",
                                                     value=st.session_state.get('non_carcinogen_threshold', ''),
                                                     key='non_carcinogen_threshold')
        if st.form_submit_button('Update Restriction'):
            cur.execute(
                "UPDATE Restriction SET 'Carcinogen Threshold' = ?,  'Non-Carcinogen Threshold' = ? WHERE "
                "RestrictionType = ?",(carcinogen_threshold, non_carcinogen_threshold, restriction_type))
            conn.commit()
            st.write("Success!")
