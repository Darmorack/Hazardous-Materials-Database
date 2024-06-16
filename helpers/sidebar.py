import streamlit as st

def show() -> None:
    with st.sidebar:
        st.markdown(f"""
    			<a href="/" style="color:black;text-decoration: none;">
    				<div style="display:table;margin-top:-16rem;margin-left:0%;">
    					<span style= "color: white">&nbsp;⚠️  HazMat</span>
    					<span style="font-size: 0.8em; color: grey">v0.1.0</span>
    					<br>
    				</div>
    			</a>
    			<br>
    				""", unsafe_allow_html=True)

    reload_button = st.sidebar.button("↪︎  Reload Page")
    if reload_button:
        st.session_state.clear()
        st.experimental_rerun()
