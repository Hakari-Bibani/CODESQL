# theme.py - Manages dark mode theme for the entire app
import streamlit as st

def apply_dark_theme():
    st.markdown(
        """
        <style>
        body {
            background-color: #121212;
            color: #ffffff;
        }

        /* Streamlit default elements */
        .stTextInput > label, .stButton > button, .stSelectbox > label {
            color: white !important;
        }
        .stTextInput, .stSelectbox, .stButton > button {
            background-color: #1e1e1e !important;
            color: white !important;
            border-radius: 5px;
            border: 1px solid #444;
        }
        .stButton > button:hover {
            background-color: #ff4757 !important;
            color: #fff !important;
        }

        /* Scrollbars */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #1e1e1e;
        }
        ::-webkit-scrollbar-thumb {
            background-color: #3e3e3e;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
