# sidebar.py - Handles sidebar navigation with an expander/accordion style
import streamlit as st

def show_sidebar():
    selected = None

    with st.sidebar:
        st.title("AI For Impact")

        # Home button (directly visible)
        if st.button("Home"):
            selected = "home"

        # Expandable section for Assignments
        with st.expander("Assignments", expanded=True):
            if st.button("Assignment 1"):
                selected = "as1"
            if st.button("Assignment 2"):
                selected = "as2"
            if st.button("Assignment 3"):
                selected = "as3"
            if st.button("Assignment 4"):
                selected = "as4"

        # Expandable section for Quizzes
        with st.expander("Quizzes", expanded=True):
            if st.button("Quiz 1"):
                selected = "quiz1"
            if st.button("Quiz 2"):
                selected = "quiz2"

        # Help and Logout buttons
        if st.button("Help"):
            selected = "help"
        if st.button("Logout"):
            selected = "logout"

    # Fallback in case no button was clicked; default to home
    if selected is None:
        selected = "home"

    return selected
