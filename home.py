import streamlit as st
from streamlit_lottie import st_lottie
import json
from theme import apply_dark_theme
from style import apply_custom_styles

def load_lottie_animation(filepath: str):
    """Loads a Lottie animation from a local JSON file."""
    with open(filepath, "r") as f:
        return json.load(f)

def show_home():
    apply_dark_theme()      # Ensures background is dark
    apply_custom_styles()   # Ensures animated title/footer style

    st.markdown('<div class="title">🌟 Welcome to AI for Impact</div>', unsafe_allow_html=True)

    # Load and display Lottie animation (Forcing Transparency)
    lottie_animation = load_lottie_animation("animation.json")  # Load from local file
    st_lottie(lottie_animation, speed=1, height=200, width=200, key="ai_animation", background="rgba(0,0,0,0)")

    # Video Section
    video_url = "https://www.youtube.com/watch?v=YOUR_REAL_VIDEO_LINK"
    st.video(video_url)

    # Footer
    st.markdown('<div class="footer">📌 Access Quizzes and Assignments via the Sidebar</div>', unsafe_allow_html=True)
    st.markdown('<div class="footer">💡 AI For Impact © 2025 - Your Partner in Academic Success</div>', unsafe_allow_html=True)
