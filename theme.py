import streamlit as st

def apply_dark_theme():
    dark_style = """
    <style>
    html, body, [class^="st-"], [class*=" st-"] {
        background-color: #121212 !important;
        color: #ffffff !important;
    }
    
    .title {
        color: #ff4757 !important;
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
        color: #bdc3c7 !important;
        margin-top: 2rem;
    }
    
    /* Force dark mode on widgets */
    .stTextInput, .stButton, .stSelectbox, .stCheckbox {
        filter: invert(1);
    }
    
    /* Hide scrollbar for better UI */
    ::-webkit-scrollbar {
        display: none;
    }
    
    </style>
    """
    st.markdown(dark_style, unsafe_allow_html=True)
