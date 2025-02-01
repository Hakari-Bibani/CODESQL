# style2.py - Adapted to match dark mode
import streamlit as st

def set_page_style():
    st.markdown(
        """
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #121212;
                color: #ffffff;
            }
            .stButton > button {
                background-color: #32CD32;
                color: white;
                font-size: 16px;
                padding: 10px 20px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
            }
            .stButton > button:hover {
                background-color: #228B22;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
