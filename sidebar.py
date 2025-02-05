import streamlit as st

def show_sidebar():
    st.title("🎈 Code for Impact")

    # Home Button
    if st.button("🏠 Home"):
        return "home"

    # Assignments Section with Expander
    with st.expander("📚 Assignments", expanded=True):
        if st.button("Assignment 1"):
            return "as1"
        if st.button("Assignment 2"):
            return "as2"
        if st.button("Assignment 3"):
            return "as3"
        if st.button("Assignment 4"):
            return "as4"

    # Quizzes Section with Expander
    with st.expander("📝 Quizzes", expanded=True):
        if st.button("Quiz 1"):
            return "quiz1"
        if st.button("Quiz 2"):
            return "quiz2"

    # Help Button
    if st.button("❓ Help"):
        return "help"

    # Logout Button
    if st.button("🔓 Logout"):
        return "logout"

    return "home"  # Default to home if nothing is selected
