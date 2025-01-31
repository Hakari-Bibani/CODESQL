''' theme.py - Manages dark mode theme for the entire app '''
import streamlit as st

def apply_dark_theme():
    st.markdown(
        '''
        <style>
        /* Apply dark background */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"],
        .block-container, .stApp {
            background-color: #121212 !important;
            color: #ffffff !important;
        }

        /* Set font to green */
        .stTextInput > label, .stSelectbox > label, .stButton > button {
            color: #32CD32 !important;  /* Light Green */
            font-weight: bold;
        }

        /* Text Input Box Improvements */
        .stTextInput, .stSelectbox, .stButton > button {
            background-color: #1e1e1e !important;
            color: white !important;
            border-radius: 8px !important;  /* Rounded corners */
            border: 1px solid #32CD32 !important; /* Green border */
            padding: 10px;
            box-shadow: 0px 0px 5px rgba(50, 205, 50, 0.5); /* Soft glow */
        }

        /* Hover effect on buttons */
        .stButton > button:hover {
            background-color: #32CD32 !important;
            color: black !important;
            transition: 0.3s ease-in-out;
        }

        /* Styling for login and create account tabs */
        div[data-testid="stTabs"] button {
            border-radius: 50px !important;  /* Make tabs rounded */
            padding: 10px 20px !important;
            font-weight: bold !important;
            color: white !important;
            background-color: #1e1e1e !important;
            border: 2px solid #32CD32 !important;
        }

        div[data-testid="stTabs"] button[aria-selected="true"] {
            background-color: #32CD32 !important;
            color: black !important;
        }
        
        /* Custom Error Message Styling */
        .error-text {
            color: #FF6347 !important; /* Red */
            font-weight: bold !important;
        }
        
        /* Scrollbar Customization */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #1e1e1e;
        }
        ::-webkit-scrollbar-thumb {
            background-color: #32CD32;
            border-radius: 10px;
        }
        </style>
        ''',
        unsafe_allow_html=True
    )
