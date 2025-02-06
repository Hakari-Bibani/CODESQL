import streamlit as st
from theme import apply_dark_theme
from style import apply_custom_styles
import json
from streamlit_lottie import st_lottie

# Function to load Lottie animation
def load_lottie_animation(filepath):
    with open(filepath, "r") as file:
        return json.load(file)

def show_home():
    apply_dark_theme()      # ensures background is dark
    apply_custom_styles()   # ensures animated title/footer style

    st.markdown('<div class="title">🌟 Welcome to AI for Impact</div>', unsafe_allow_html=True)

    # Load Lottie Animation
    animation_path = "8BJkB4IiSL.json"  # Ensure this file is in the repository and accessible
    lottie_animation = load_lottie_animation(animation_path)

    # Custom CSS for Centering Animation in Black Background Box
    st.markdown(
        """
        <style>
        .animation-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 350px;
            background-color: black;
            border-radius: 15px;
            padding: 20px;
            margin: 20px auto;
            width: 60%;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display Lottie Animation in Centered Black Box
    st.markdown('<div class="animation-container">', unsafe_allow_html=True)
    st_lottie(lottie_animation, speed=1, loop=True, height=250, width=250)
    st.markdown('</div>', unsafe_allow_html=True)

    # Polished Footer Messages with Custom Colors
    st.markdown('<div class="footer footer-assignments">📌 Access Quizzes and Assignments via the Sidebar</div>', unsafe_allow_html=True)
    st.markdown('<div class="footer footer-partner">💡 AI For Impact © 2025 - Your Partner in Academic Success</div>', unsafe_allow_html=True)

