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
    apply_dark_theme()  # ensures dark background
    apply_custom_styles()  # custom styles

    # Custom CSS to center animation & remove white background
    st.markdown(
        """
        <style>
            .lottie-container {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            iframe {
                background: transparent !important;
            }
            .stApp {
                background-color: black !important;  /* Force full black background */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="title">🌟 Welcome to AI for Impact</div>', unsafe_allow_html=True)

    # Load and Display Lottie Animation
    animation_path = "8BJkB4IiSL.json"
    lottie_animation = load_lottie_animation(animation_path)

    # Centering the animation
    st.markdown('<div class="lottie-container">', unsafe_allow_html=True)
    st_lottie(lottie_animation, speed=1, loop=True, height=300, width=300, key="animation")  # Removed background="transparent"
    st.markdown('</div>', unsafe_allow_html=True)

    # Footer messages
    st.markdown('<div class="footer footer-assignments">📌 Access Quizzes and Assignments via the Sidebar</div>', unsafe_allow_html=True)
    st.markdown('<div class="footer footer-partner">💡 AI For Impact © 2025 - Your Partner in Academic Success</div>', unsafe_allow_html=True)
