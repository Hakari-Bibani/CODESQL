import streamlit as st

def show_sidebar():
    # Custom CSS for the sidebar styling with enhanced title
    st.markdown("""
        <style>
        /* Advanced Title Styling */
        .sidebar-title {
            background: linear-gradient(45deg, #1e3c72, #2a5298);
            padding: 20px 10px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .sidebar-title h1 {
            color: white !important;
            font-size: 24px !important;
            font-weight: 600 !important;
            margin: 0 !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        .app-subtitle {
            color: #E0E0E0 !important;
            font-size: 14px !important;
            margin-top: 5px !important;
            font-style: italic;
        }
        
        /* Expander Styling */
        .stExpander {
            border: 1px solid #4B4B4B !important;
            border-radius: 5px !important;
            margin-bottom: 10px !important;
            transition: all 0.3s ease !important;
        }
        .stExpander:hover {
            border-color: #6B6B6B !important;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2) !important;
        }
        .stExpander > div:first-child {
            background-color: #2E2E2E !important;
            padding: 10px 15px !important;
        }
        
        /* Button Styling */
        .stButton button {
            transition: all 0.3s ease !important;
        }
        .stButton button:hover {
            transform: translateX(5px) !important;
            background-color: #4A4A4A !important;
        }
        </style>
        """, unsafe_allow_html=True)

    with st.sidebar:
        # Custom title with gradient background
        st.markdown('''
            <div class="sidebar-title">
                <h1>AI For Impact</h1>
                <p class="app-subtitle">Empowering Learning Through AI</p>
            </div>
        ''', unsafe_allow_html=True)
        
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
