import streamlit as st
from streamlit_lottie import st_lottie
import json
from theme import apply_dark_theme
from style import apply_custom_styles

def load_lottie_animation(path: str):
    """Loads a Lottie animation from a local JSON file."""
    with open(path, "r") as f:
        return json.load(f)

def show_home():
    apply_dark_theme()      # ensures background is dark
    apply_custom_styles()   # ensures animated title/footer style

    st.markdown('<div class="title">🌟 Welcome to AI for Impact</div>', unsafe_allow_html=True)

    # Load Lottie animation
    lottie_animation = load_lottie_animation("animation.json")

    # Centered Animation with Transparent Background
    st.markdown(
        """
        <style>
        .lottie-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: -20px;
        }
        </style>
        <div class="lottie-container">
        """,
        unsafe_allow_html=True,
    )

    # Display Lottie Animation
    st_lottie(lottie_animation, speed=1, width=150, height=150, key="ai_animation")  # Removed background=None

    st.markdown("</div>", unsafe_allow_html=True)

    # Video Section
    video_url = "https://www.youtube.com/watch?v=YOUR_REAL_VIDEO_LINK"
    st.video(video_url)

    # Footer
    st.markdown('<div class="footer">📌Access Quizzes and Assignments via the Sidebar</div>', unsafe_allow_html=True)
    st.markdown('<div class="footer">💡AI For Impact © 2025 - Your Partner in Academic Success</div>', unsafe_allow_html=True)
