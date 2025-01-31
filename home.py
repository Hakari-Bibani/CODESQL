import streamlit as st
from streamlit_lottie import st_lottie
import json
from theme import apply_dark_theme
from style import apply_custom_styles

def load_lottie_animation(filepath: str):
    """Loads a Lottie animation from a JSON file."""
    with open(filepath, "r") as f:
        return json.load(f)

def show_home():
    apply_dark_theme()      # ensures background is dark
    apply_custom_styles()   # ensures animated title/footer style

    st.markdown('<div class="title">🌟 Welcome to AI for Impact</div>', unsafe_allow_html=True)

    # Load and display Lottie animation
    animation = load_lottie_animation("animation.json")  # Ensure the file is in the main directory
    st_lottie(animation, speed=1, loop=True, quality="high", height=300, width=300)

    # Video Section
    video_url = "https://www.youtube.com/watch?v=YOUR_REAL_VIDEO_LINK"
    st.video(video_url)

    # Footer
    st.markdown('<div class="footer">📌 Access Quizzes and Assignments via the Sidebar</div>', unsafe_allow_html=True)
    st.markdown('<div class="footer">💡 AI For Impact © 2025 - Your Partner in Academic Success</div>', unsafe_allow_html=True)
