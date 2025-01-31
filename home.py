import streamlit as st
from streamlit_lottie import st_lottie
import requests
from theme import apply_dark_theme
from style import apply_custom_styles

# Load Lottie animation from GitHub
def load_lottie_animation(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def show_home():
    apply_dark_theme()      # Ensures background is dark
    apply_custom_styles()   # Ensures animated title/footer style

    st.markdown('<div class="title">🌟 Welcome to AI for Impact</div>', unsafe_allow_html=True)

    # Load Lottie animation from GitHub (Replace 'YOUR_GITHUB_USERNAME' & 'YOUR_REPO')
    animation_url = "https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_REPO/main/animation.json"
    lottie_animation = load_lottie_animation(animation_url)

    # Display animation with transparency and resizable properties
    if lottie_animation:
        st_lottie(lottie_animation, key="lottie_home", speed=1, width=400, height=400, loop=True, background_color=None)

    # Video
    video_url = "https://www.youtube.com/watch?v=YOUR_REAL_VIDEO_LINK"
    st.video(video_url)

    # Footer
    st.markdown('<div class="footer">📌 Access Quizzes and Assignments via the Sidebar</div>', unsafe_allow_html=True)
    st.markdown('<div class="footer">💡 AI For Impact © 2025 - Your Partner in Academic Success</div>', unsafe_allow_html=True)
