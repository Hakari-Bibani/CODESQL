import streamlit as st

def show_sidebar():
    # Custom CSS for the sidebar styling
    st.markdown("""
        <style>
        .stExpander {
            border: 1px solid #4B4B4B !important;
            border-radius: 5px !important;
            margin-bottom: 10px !important;
        }
        .stExpander > div:first-child {
            background-color: #2E2E2E !important;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.title("AI For Impact")
        
        # Home section
        with st.expander("🏠 HOME", expanded=False):
            if st.button("Home Page", key="home", use_container_width=True):
                st.session_state["page"] = "home"
        
        # Assignments section
        with st.expander("📚 ASSIGNMENTS", expanded=False):
            if st.button("Assignment 1", key="as1", use_container_width=True):
                st.session_state["page"] = "as1"
            if st.button("Assignment 2", key="as2", use_container_width=True):
                st.session_state["page"] = "as2"
            if st.button("Assignment 3", key="as3", use_container_width=True):
                st.session_state["page"] = "as3"
            if st.button("Assignment 4", key="as4", use_container_width=True):
                st.session_state["page"] = "as4"
        
        # Quizzes section
        with st.expander("📝 QUIZZES", expanded=False):
            if st.button("Quiz 1", key="quiz1", use_container_width=True):
                st.session_state["page"] = "quiz1"
            if st.button("Quiz 2", key="quiz2", use_container_width=True):
                st.session_state["page"] = "quiz2"
        
        # Help section
        with st.expander("❓ HELP", expanded=False):
            if st.button("Help Center", key="help", use_container_width=True):
                st.session_state["page"] = "help"
        
        # Logout section
        with st.expander("🚪 LOGOUT", expanded=False):
            if st.button("Logout", key="logout", use_container_width=True):
                st.session_state["page"] = "logout"

        # Return the current page
        return st.session_state.get("page", "home")
