''' style.py - Manages global styles (Dark Theme) '''
import streamlit as st

def apply_dark_theme():
    """Applies a consistent dark theme across the app."""
    st.markdown("""
        <style>
        body {
            background-color: #121212;
            color: white;
        }
        .title {
            color: #ff4757;
            font-size: 2.5rem;
            font-weight: bold;
            text-align: center;
            animation: move 2s infinite;
            margin-bottom: 1rem;
        }
        @keyframes move {
            0% { transform: translateX(0); }
            50% { transform: translateX(10px); }
            100% { transform: translateX(0); }
        }
        .footer {
            text-align: center;
            font-size: 1.2rem;
            color: #bdc3c7;
            margin-top: 2rem;
        }
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
        }
        </style>
    """, unsafe_allow_html=True)
