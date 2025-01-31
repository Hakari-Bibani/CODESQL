import streamlit as st
from theme import apply_dark_theme
from database import create_tables
from login import show_login_create_account
from sidebar import show_sidebar
from home import show_home

def main():
    # 1) Must be the FIRST Streamlit command
    st.set_page_config(page_title="Code for Impact", layout="wide")

    # 2) Apply dark theme CSS next
    apply_dark_theme()
    
    create_tables()

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if st.session_state["logged_in"]:
        selected = show_sidebar()

        if selected == "logout":
            st.session_state["logged_in"] = False
            st.rerun()
        elif selected == "home":
            show_home()
        else:
            st.warning("Unknown selection.")
    else:
        show_login_create_account()

if __name__ == "__main__":
    main()
