import streamlit as st
from theme import apply_dark_theme
from style import apply_custom_styles
from streamlit_lottie import st_lottie
import json

def load_lottie_animation():
    """Loads the Lottie animation from a JSON file."""
    try:
        with open("animation.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("⚠️ Animation file not found!")
        return None

def show_home():
    apply_dark_theme()      # ensures background is dark
    apply_custom_styles()   # ensures animated title/footer style

    st.markdown('<div class="title">🌟 Welcome to AI for Impact</div>', unsafe_allow_html=True)

    # Load and display Lottie animation with a transparent background
    lottie_animation = load_lottie_animation()
    if lottie_animation:
        st_lottie(
            lottie_animation,
            speed=1,               # Adjust animation speed
            loop=True,             # Set to True to make it loop continuously
            quality="high",        # Options: "low", "medium", "high"
            key="ai_animation"     # Unique key for Streamlit component
        )

    # Video
    video_url = "https://www.youtube.com/watch?v=YOUR_REAL_VIDEO_LINK"
    st.video(video_url)

    # Footer
    st.markdown('<div class="footer">📌Access Quizzes and Assignments via the Sidebar</div>', unsafe_allow_html=True)
    st.markdown('<div class="footer">💡AI For Impact © 2025 - Your Partner in Academic Success</div>', unsafe_allow_html=True)
