import streamlit as st
from theme import apply_dark_theme
from style import apply_custom_styles

def show_home():
    apply_dark_theme()      # ensures background is dark
    apply_custom_styles()   # ensures animated title/footer style

    st.markdown('<div class="title">🌟 Welcome to AI for Impact</div>', unsafe_allow_html=True)

    # Lottie Animation (Replace with your actual repository raw link)
    animation_url = "https://raw.githubusercontent.com/Hakari-Bibani/WGSQL/main/8BJkB4IiSL.json"

    lottie_html = f"""
    <script src="https://unpkg.com/@dotlottie/player-component@2.7.12/dist/dotlottie-player.mjs" type="module"></script>
    <dotlottie-player 
        src="{animation_url}" 
        background="transparent" 
        speed="1" 
        style="width: 300px; height: 300px" 
        loop autoplay>
    </dotlottie-player>
    """
    st.markdown(lottie_html, unsafe_allow_html=True)

    # Polished Footer Messages with Custom Colors
    st.markdown('<div class="footer footer-assignments">📌 Access Quizzes and Assignments via the Sidebar</div>', unsafe_allow_html=True)
    st.markdown('<div class="footer footer-partner">💡 AI For Impact © 2025 - Your Partner in Academic Success</div>', unsafe_allow_html=True)
