# style.py - Extra custom styles (animations, text, etc.)
import streamlit as st

def apply_custom_styles():
    # Example of custom CSS for animated title, etc.
    st.markdown(
        """
        <style>
        /* Animation for moving text */
        @keyframes move {
            0% { transform: translateX(0); }
            50% { transform: translateX(10px); }
            100% { transform: translateX(0); }
        }

        /* Title style */
        .title {
            color: #ff4757;
            font-size: 2.5rem;
            font-weight: bold;
            text-align: center;
            animation: move 2s infinite;
            margin-bottom: 1rem;
        }
        
        /* Footer text */
        .footer {
            text-align: center;
            font-size: 1.2rem;
            color: #bdc3c7;
            margin-top: 2rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
