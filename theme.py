# theme.py - Manages dark mode theme for the entire app, including sidebar and animations
import streamlit as st

def apply_dark_theme():
    st.markdown(
        '''
        <style>
        /* Apply dark background globally */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"],
        .block-container, .stApp {
            background-color: #121212 !important;
            color: #ffffff !important;
        }

        /* Resize Lottie Animation Container */
        .lottie-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
        }

        .lottie-animation {
            max-width: 200px !important;
            max-height: 200px !important;
            margin: auto;
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"], .sidebar-content {
            background-color: #1e1e1e !important;
            color: #ffffff !important;
            border-right: 1px solid #32CD32 !important;
        }

        [data-testid="stSidebar"] div {
            color: white !important;
        }
        
        /* Sidebar menu item styling */
        .css-1d391kg, .css-18e3th9 {
            color: white !important;
        }
        
        /* Sidebar menu hover effect */
        .css-1d391kg:hover, .css-18e3th9:hover {
            background-color: #32CD32 !important;
            color: black !important;
            border-radius: 8px;
            transition: 0.3s ease-in-out;
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
