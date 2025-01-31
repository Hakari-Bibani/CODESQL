import streamlit as st

def apply_dark_theme():
    st.markdown("""
        <style>
        body {
            background-color: #121212;
            color: #ffffff;
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
        .stSidebar {
            background-color: #b0b0b0 !important;
        }
        </style>
    """, unsafe_allow_html=True)
