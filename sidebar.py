import streamlit as st

def show_sidebar():
    with st.sidebar:
        st.title("AI For Impact")
        
        # Home section
        st.button("🏠 Home", key="home", use_container_width=True, 
                 on_click=lambda: st.session_state.update({"page": "home"}))
        
        # Assignments section
        with st.expander("📚 ASSIGNMENTS", expanded=True):
            st.button("Assignment 1", key="as1", use_container_width=True,
                     on_click=lambda: st.session_state.update({"page": "as1"}))
            st.button("Assignment 2", key="as2", use_container_width=True,
                     on_click=lambda: st.session_state.update({"page": "as2"}))
            st.button("Assignment 3", key="as3", use_container_width=True,
                     on_click=lambda: st.session_state.update({"page": "as3"}))
            st.button("Assignment 4", key="as4", use_container_width=True,
                     on_click=lambda: st.session_state.update({"page": "as4"}))
        
        # Quizzes section
        with st.expander("📝 QUIZZES", expanded=True):
            st.button("Quiz 1", key="quiz1", use_container_width=True,
                     on_click=lambda: st.session_state.update({"page": "quiz1"}))
            st.button("Quiz 2", key="quiz2", use_container_width=True,
                     on_click=lambda: st.session_state.update({"page": "quiz2"}))
        
        # Help and Logout
        st.button("❓ Help", key="help", use_container_width=True,
                 on_click=lambda: st.session_state.update({"page": "help"}))
        st.button("🚪 Logout", key="logout", use_container_width=True,
                 on_click=lambda: st.session_state.update({"page": "logout"}))

        # Return the current page
        return st.session_state.get("page", "home")
