import streamlit as st
from theme import apply_dark_theme

def show_home():
    apply_dark_theme()
    st.markdown('<div class="title">Welcome to Code for Impact</div>', unsafe_allow_html=True)
    
    # Video Section
    video_url = "https://www.youtube.com/watch?v=YOUR_REAL_VIDEO_LINK"
    st.video(video_url)
    
    # Footer Text
    st.markdown('<div class="footer">Access Quizzes and Assignments via the Sidebar</div>', unsafe_allow_html=True)
    st.markdown('<div class="footer">Code For Impact © 2025 - Your Partner in Academic Success</div>', unsafe_allow_html=True)
