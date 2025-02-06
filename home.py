import streamlit as st
import json
from streamlit_lottie import st_lottie

def load_lottie_from_file(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

def show_home():
    st.markdown("""
        <style>
            .stApp { background-color: black !important; }
            iframe {
                background: none !important;
                box-shadow: none !important;
            }
        </style>
    """, unsafe_allow_html=True)

    lottie_animation = load_lottie_from_file("8BJkB4IiSL.json")

    if lottie_animation:
        st_lottie(lottie_animation, key="animation", height=300, width=300)
    else:
        st.error("Failed to load animation.")
