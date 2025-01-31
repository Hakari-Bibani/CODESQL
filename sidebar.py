import streamlit as st
from streamlit_option_menu import option_menu

def show_sidebar():
    st.markdown("""
        <style>
            /* Sidebar Background */
            [data-testid="stSidebar"] {
                background-color: #1B5E20 !important;
                color: white !important;
            }
            
            /* Sidebar Title */
            [data-testid="stSidebar"] h1 {
                color: #C8E6C9 !important;
                text-align: center;
                font-size: 22px !important;
                font-weight: bold;
            }
            
            /* Sidebar Menu Items */
            .css-1d391kg, .css-10trblm, .css-1v3fvcr, .css-1aumxhk {
                color: white !important;
                font-size: 18px !important;
                font-weight: bold !important;
                padding: 10px !important;
                background-color: #2E7D32 !important;
                border-radius: 8px !important;
                margin-bottom: 5px !important;
            }
            
            .css-1d391kg:hover, .css-10trblm:hover, .css-1v3fvcr:hover, .css-1aumxhk:hover {
                background-color: #388E3C !important;
                color: #C8E6C9 !important;
            }
            
            /* Sidebar Buttons */
            .stButton>button {
                background-color: #2E7D32 !important;
                color: white !important;
                border-radius: 8px !important;
                font-weight: bold !important;
                padding: 10px !important;
                border: none !important;
            }
            .stButton>button:hover {
                background-color: #388E3C !important;
                color: white !important;
            }
            
            /* Sidebar Selectbox */
            .stSelectbox div[data-baseweb="select"] {
                background-color: #1B5E20 !important;
                color: white !important;
                border-radius: 8px !important;
                font-size: 16px !important;
            }
            .stSelectbox div[data-baseweb="select"] * {
                color: white !important;
            }
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
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
