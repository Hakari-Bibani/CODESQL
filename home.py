import streamlit as st
import json
from theme import apply_dark_theme
from style import apply_custom_styles

def show_home():
    apply_dark_theme()      # ensures background is dark
    apply_custom_styles()   # ensures animated title/footer style

    st.markdown('<div class="title">🌟 Welcome to AI for Impact</div>', unsafe_allow_html=True)
    
    # Load and display JSON file
    json_file = "8BJkB4IiSL.json"
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            st.json(data)  # Display JSON data in Streamlit
    except Exception as e:
        st.error(f"Error loading JSON file: {e}")
    
    # Polished Footer Messages with Custom Colors
    st.markdown('<div class="footer footer-assignments">📌 Access Quizzes and Assignments via the Sidebar</div>', unsafe_allow_html=True)
    st.markdown('<div class="footer footer-partner">💡 AI For Impact © 2025 - Your Partner in Academic Success</div>', unsafe_allow_html=True)

# Run the function
if __name__ == "__main__":
    show_home()
