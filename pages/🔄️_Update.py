import streamlit as st
import sqlite3
import helpers.sidebar

st.set_page_config(
    page_title="Hazardous Materials Database",
    page_icon="🔄",
    layout="wide"
)

helpers.sidebar.show()


conn = sqlite3.connect('Hazardous Materials Database.db')
cur = conn.cursor()

table_options = ["Select an Option", "Item", "Action", "Substance", "Restriction"]
table_choice = st.selectbox("Which table would you like to update?", table_options)

if table_choice == "Action":
    person = ""
    status = ""
    completion_date = ""
    notes = ""

    with st.expander("Search for an Action"):
        action_id = st.text_input("Action ID")
        item_id = st.text_input("Item ID")
        if st.button('Search', key='action_search'):
            result = cur.execute(
                'SELECT "Completion Date",  "Notes", "Status", "Person" FROM Actions where ActionID = ? AND ItemID = ?',
                (action_id, item_id)).fetchone()
            completion_date = result[0]
            notes = result[1]
            status = result[2]
            person = result[3]
            st.write("Success!")
    with st.expander("Action Attributes"):
        person_input = st.text_input("Person", person)
        status_input = st.text_input("Status", status)
        completion_date_input = st.text_input("Completion Date", completion_date)
        notes_input = st.text_input("Notes", notes)
    if st.button('Update Action', key='submit_action'):
        st.write("Success!")


if table_choice == "Item":
    with st.expander("Search for an Item"):
        item_id = st.text_input("Item ID")
        if st.button('Search', key='item_search'):
            st.write("Success!")
        test = "hello"
    with st.expander("Item Attributes"):
        item_name = st.text_input("Enter Item's Name", test)
        references = st.text_input("Enter References")
        potential_for_exposure = st.text_input("Enter Potential for Exposure")
        controls_mitigations = st.text_input("Enter Controls/Mitigations")
        hazard_tracking_system_references = st.text_input("Enter Hazard/Hazard Tracking System References")
        notes = st.text_input("Enter Notes")
        quantity = st.text_input("Quantity")
        category = st.text_input("Enter Category")
    if st.button('Update Item', key='submit_item'):
        st.write("Success!")

if table_choice == "Substance":
    with st.expander("Search for a Substance"):
        substance_name = st.text_input("Substance Name")
        if st.button('Search', key='substance_search'):
            st.write("Success!")
    with st.expander("Substance Attributes"):
        restriction = st.text_input("Restriction")
        cas_numbers = st.text_input("CAS Numbers")
        name = st.text_input("Name")
    if st.button('Update Substance', key='submit_substance'):
        st.write("Success!")

if table_choice == "Restriction":
    with st.expander("Search for a Restriction"):
        restriction_name = st.text_input("Restriction Name")
        if st.button('Search', key='restriction_search'):
            st.write("Success!")
    with st.expander("Restriction Attributes"):
        carcinogen_threshold = st.text_input("Carcinogen Threshold")
        non_carcinogen_threshold = st.text_input("Non-Carcinogen Threshold")
    if st.button('Update Restriction', key='submit_restriction'):
        st.write("Success!")

