# sidebar.py
import streamlit as st

def show_sidebar():
    selection = None  # To track the selected page
    
    # Sidebar title
    st.sidebar.title("🎈 Okld's Gallery")
    
    # Home button
    if st.sidebar.button("Home"):
        selection = "home"

    # Expander for Assignments
    with st.sidebar.expander("Assignments", expanded=True):
        if st.button("Assignment 1", key="as1"):
            selection = "as1"
        if st.button("Assignment 2", key="as2"):
            selection = "as2"
        if st.button("Assignment 3", key="as3"):
            selection = "as3"
        if st.button("Assignment 4", key="as4"):
            selection = "as4"
    
    # Expander for Quizzes
    with st.sidebar.expander("Quizzes", expanded=True):
        if st.button("Quiz 1", key="quiz1"):
            selection = "quiz1"
        if st.button("Quiz 2", key="quiz2"):
            selection = "quiz2"
    
    # Help button
    if st.sidebar.button("Help"):
        selection = "help"
    
    # Logout button
    if st.sidebar.button("Logout"):
        selection = "logout"

    # Default to home if nothing was clicked
    if selection is None:
        selection = "home"
    
    return selection
