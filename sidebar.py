import streamlit as st
from streamlit_option_menu import option_menu

def show_sidebar():
    with st.sidebar:
        st.markdown("""
            <style>
                .sidebar .sidebar-content {
                    background-color: #1B5E20;
                    color: white;
                }
                .sidebar .stButton>button {
                    background-color: #2E7D32;
                    color: white;
                    border-radius: 8px;
                    font-weight: bold;
                    padding: 10px;
                }
                .sidebar .stButton>button:hover {
                    background-color: #388E3C;
                    color: white;
                }
                .sidebar .stSelectbox div[data-baseweb="select"] {
                    background-color: #1B5E20;
                    color: white;
                    border-radius: 8px;
                }
                .sidebar .stSelectbox div[data-baseweb="select"] * {
                    color: white;
                }
            </style>
        """, unsafe_allow_html=True)
        
        st.title("Code For Impact")
        
        menu_options = {
            "Home": "home",
            "Assignments": {
                "Assignment 1": "as1",
                "Assignment 2": "as2",
                "Assignment 3": "as3",
                "Assignment 4": "as4",
            },
            "Quizzes": {
                "Quiz 1": "quiz1",
                "Quiz 2": "quiz2",
            },
            "Help": "help",
            "Logout": "logout"
        }
        
        selected = option_menu(
            menu_title=None,
            options=list(menu_options.keys()),
            icons=["house", "book", "pencil-square", "question-circle", "box-arrow-right"],
            menu_icon="cast",
            default_index=0,
            orientation="vertical",
        )

        if selected in ["Assignments", "Quizzes"]:
            sub_options = ["Select"] + list(menu_options[selected].keys())
            sub_selected = st.selectbox(f"Select a {selected[:-1]}", sub_options, key=f"{selected}_selection")
            if sub_selected != "Select":
                return menu_options[selected][sub_selected]  # Return selected sub-option
            else:
                return "home"  # Stay on home page if no selection
        
        return menu_options[selected]  # Return main selection if not Assignments/Quizzes
