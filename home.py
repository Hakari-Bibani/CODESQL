import streamlit as st
import json
import os
from theme import apply_dark_theme
from style import apply_custom_styles

# Function to load and display JSON content
def load_json_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    else:
        return {"error": "JSON file not found."}

def show_home():
    apply_dark_theme()      # ensures background is dark
    apply_custom_styles()   # ensures animated title/footer style

    st.markdown('<div class="title">🌟 Welcome to AI for Impact</div>', unsafe_allow_html=True)

    # Path to JSON file in the repository
    json_file_path = "8BJkB4IiSL.json"
    
    # Load and display JSON content
    json_data = load_json_file(json_file_path)
    st.json(json_data)

    # Polished Footer Messages with Custom Colors
    st.markdown('<div class="footer footer-assignments">📌 Access Quizzes and Assignments via the Sidebar</div>', unsafe_allow_html=True)
    st.markdown('<div class="footer footer-partner">💡 AI For Impact © 2025 - Your Partner in Academic Success</div>', unsafe_allow_html=True)
