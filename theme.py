# theme.py - Manages dark mode theme for the entire app
import streamlit as st

def apply_dark_theme():
    # IMPORTANT: Make sure st.set_page_config() is called in your main script
    # before any Streamlit command. Do NOT call it here, or you'll trigger the
    # 'SetPageConfigMustBeFirstCommandError' if anything else has run first.

    st.markdown(
        '''
        <style>
        /* Force dark background across main containers in newer Streamlit versions */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"],
        .block-container, .stApp {
            background-color: #121212 !important;
            color: #ffffff !important;
        }

        /* Default text elements */
        .stText, .stMarkdown, .stException {
            color: #ffffff !important;
        }

        /* Input labels, buttons, selects */
        .stTextInput > label, .stSelectbox > label, .stButton > button {
            color: #ffffff !important;
        }
        .stTextInput, .stSelectbox, .stButton > button {
            background-color: #1e1e1e !important;
            border: 1px solid #444 !important;
            color: #ffffff !important;
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
        ''',
        unsafe_allow_html=True
    )
