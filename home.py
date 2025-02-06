import streamlit as st
import requests
import json
from theme import apply_dark_theme
from style import apply_custom_styles
from streamlit_lottie import st_lottie

def load_lottie_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def load_lottie_from_file(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

def show_home():
    apply_dark_theme()      # ensures background is dark
    apply_custom_styles()   # ensures animated title/footer style

    st.markdown('<div class="title">🌟 Welcome to AI for Impact</div>', unsafe_allow_html=True)

    # Load Lottie Animation from JSON File
    lottie_animation = load_lottie_from_file("8BJkB4IiSL.json")
    
    if lottie_animation:
        st_lottie(lottie_animation, height=300, width=400)
    else:
        st.error("Failed to load animation.")

    # Polished Footer Messages with Custom Colors
    st.markdown('<div class="footer footer-assignments">📌 Access Quizzes and Assignments via the Sidebar</div>', unsafe_allow_html=True)
    st.markdown('<div class="footer footer-partner">💡 AI For Impact © 2025 - Your Partner in Academic Success</div>', unsafe_allow_html=True)

