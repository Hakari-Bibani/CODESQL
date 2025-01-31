''' app.py - Main entry point '''
import streamlit as st
from database import create_tables
from login import show_login_create_account
from sidebar import show_sidebar
from home import show_home

def main():
    st.set_page_config(page_title="Code for Impact", layout="wide")
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

    # Footer
    st.markdown("""
        <div style="text-align: center; margin-top: 50px; padding: 20px; font-size: 0.9em; color: #666;">
            Code For Impact © 2025 - Your Partner in Academic Success
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

