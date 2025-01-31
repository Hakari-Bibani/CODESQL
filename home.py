import streamlit as st
from theme import apply_dark_theme
from style import apply_custom_styles
from streamlit_lottie import st_lottie
import json
import os

def load_lottie_animation(filepath: str):
    """Load Lottie animation from a JSON file."""
    with open(filepath, "r") as f:
        return json.load(f)

def show_home():
    apply_dark_theme()      # Ensures background is dark
    apply_custom_styles()   # Ensures animated title/footer style

    st.markdown('<div class="title">🌟 Welcome to AI for Impact</div>', unsafe_allow_html=True)

    # Load and display the Lottie animation
    animation_path = os.path.join(os.getcwd(), "animation.json")  # Adjust path if needed
    lottie_animation = load_lottie_animation(animation_path)

    # Display animation with custom size (width=300, height=300) and no background
    st_lottie(lottie_animation, speed=1, width=300, height=300, key="ai_animation")

    # Video
    video_url = "https://www.youtube.com/watch?v=YOUR_REAL_VIDEO_LINK"
    st.video(video_url)

    # Footer
    st.markdown('<div class="footer">📌Access Quizzes and Assignments via the Sidebar</div>', unsafe_allow_html=True)
    st.markdown('<div class="footer">💡AI For Impact © 2025 - Your Partner in Academic Success</div>', unsafe_allow_html=True)
