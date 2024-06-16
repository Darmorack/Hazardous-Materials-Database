import streamlit as st
import sqlite3
import helpers.sidebar

st.set_page_config(
    page_title="Hazardous Materials Database",
    page_icon="➕",
    layout="wide"
)

helpers.sidebar.show()


@st.cache_resource
def init_connection():
    return sqlite3.connect('Hazardous Materials Database.db')


conn = init_connection()

# Initialize the session state
if "item_submitted" not in st.session_state:
    st.session_state["item_submitted"] = False
    st.session_state["subsystem_submitted"] = False
    st.session_state["item_data"] = {}
    st.session_state["subsystem_data"] = {}

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



# if table_choice == "Item" and not st.session_state["item_submitted"]:
#     item_id = st.text_input("Enter Item's ID", value=st.session_state["item_data"].get("item_id", ""))
#     references = st.text_input("Enter References", value=st.session_state["item_data"].get("references", ""))
#     potential_for_exposure = st.text_input("Enter Potential for Exposure",
#                                            value=st.session_state["item_data"].get("potential_for_exposure", ""))
#     controls_mitigations = st.text_input("Enter Controls/Mitigations",
#                                          value=st.session_state["item_data"].get("controls_mitigations", ""))
#     hazard_tracking_system_references = st.text_input("Enter Hazard/Hazard Tracking System References",
#                                                       value=st.session_state["item_data"].get(
#                                                           "hazard_tracking_system_references", ""))
#     notes = st.text_input("Enter Notes", value=st.session_state["item_data"].get("notes", ""))
#     quantity = st.text_input("Enter Quantity", value=st.session_state["item_data"].get("quantity", ""))
#     category = st.text_input("Enter Category", value=st.session_state["item_data"].get("category", ""))
#
#     col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
#     with col4:
#         if st.button('Continue', key='item_continue'):
#             # Store the entered values in their respective variables
#             st.session_state["item_data"] = {
#                 "item_id": item_id,
#                 "references": references,
#                 "potential_for_exposure": potential_for_exposure,
#                 "controls_mitigations": controls_mitigations,
#                 "hazard_tracking_system_references": hazard_tracking_system_references,
#                 "notes": notes,
#                 "quantity": quantity,
#                 "category": category
#             }
#
#         # Set the item_submitted state to True
#     st.session_state["item_submitted"] = True
#
# if st.session_state["item_submitted"] and not st.session_state["subsystem_submitted"]:
#     # Display new text input fields for the subsystem information
#     subsystem_name = st.text_input("Enter Subsystem Name", value=st.session_state["subsystem_data"].get("subsystem_name", ""))
#
#     col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
#
#     with col4:
#         if st.button('Continue', key='subsystem_continue'):
#             # Store the entered values in their respective variables
#             st.session_state["subsystem_data"] = {
#                 "subsystem_name": subsystem_name,
#             }
#
#             # Set the subsystem_submitted state to True
#             st.session_state["subsystem_submitted"] = True
#
#     with col1:
#         if st.button('Back', key='back_button'):
#             # Set the item_submitted state back to False
#             st.session_state["item_submitted"] = False
#             st.session_state["subsystem_submitted"] = False
