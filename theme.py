import streamlit as st

def apply_dark_theme():
    dark_style = """
    <style>
    body {
        background-color: #121212;
        color: #ffffff;
    }
    .title {
        color: #ff4757;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        animation: move 2s infinite;
        margin-bottom: 1rem;
    }
    @keyframes move {
        0% { transform: translateX(0); }
        50% { transform: translateX(10px); }
        100% { transform: translateX(0); }
    }
    .footer {
        text-align: center;
        font-size: 1.2rem;
        color: #bdc3c7;
        margin-top: 2rem;
    }
    </style>
    """
    st.markdown(dark_style, unsafe_allow_html=True)

''' home.py - Displays homepage '''
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
