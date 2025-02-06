import streamlit as st
import json
from theme import apply_dark_theme
from style import apply_custom_styles

def show_home():
    apply_dark_theme()      # ensures background is dark
    apply_custom_styles()   # ensures animated title/footer style

    st.markdown('<div class="title">🌟 Welcome to AI for Impact</div>', unsafe_allow_html=True)

    # Load video URL from JSON file
    try:
        with open("8BJkB4IiSL.json", "r") as file:
            data = json.load(file)
            video_url = data.get("video_url", "")  # Ensure the key matches your JSON structure
    except Exception as e:
        video_url = ""
        st.error("Failed to load video. Please check the JSON file.")

    # Display the video if URL is available
    if video_url:
        st.video(video_url)
    else:
        st.warning("No video URL found in the JSON file.")

    # Polished Footer Messages with Custom Colors
    st.markdown('<div class="footer footer-assignments">📌 Access Quizzes and Assignments via the Sidebar</div>', unsafe_allow_html=True)
    st.markdown('<div class="footer footer-partner">💡 AI For Impact © 2025 - Your Partner in Academic Success</div>', unsafe_allow_html=True)
