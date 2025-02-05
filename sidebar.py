import streamlit as st
from streamlit_option_menu import option_menu

def show_sidebar():
    with st.sidebar:
        # Sidebar Title
        st.markdown("### 🎈 Code for Impact")

        # Main Menu Options
        selected = option_menu(
            menu_title=None,
            options=["Home", "Assignments", "Quizzes", "Help", "Logout"],
            icons=["house", "book", "pencil-square", "question-circle", "box-arrow-right"],
            menu_icon="cast",
            default_index=0,
            orientation="vertical",
            styles={
                "container": {"padding": "5px", "background-color": "#1e1e1e"},
                "icon": {"color": "orange", "font-size": "20px"}, 
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "5px",
                    "color": "white",
                    "border-radius": "10px"
                },
                "nav-link-selected": {
                    "background-color": "#4b4b4b",
                    "color": "white",
                    "font-weight": "bold"
                }
            }
        )

        # Handle Sub-Menus
        if selected == "Assignments":
            assignment = st.selectbox("Select Assignment", ["Assignment 1", "Assignment 2", "Assignment 3", "Assignment 4"])
            return {"Assignment 1": "as1", "Assignment 2": "as2", "Assignment 3": "as3", "Assignment 4": "as4"}[assignment]

        elif selected == "Quizzes":
            quiz = st.selectbox("Select Quiz", ["Quiz 1", "Quiz 2"])
            return {"Quiz 1": "quiz1", "Quiz 2": "quiz2"}[quiz]

        # Return the selection for other options
        return selected.lower()
