import streamlit as st

def show_sidebar():
    # Custom CSS for section styling
    st.markdown("""
        <style>
        .sidebar-section {
            padding: 10px;
            margin: 10px 0;
            border-bottom: 1px solid #4B4B4B;
        }
        .section-title {
            font-size: 1.2em;
            font-weight: bold;
            margin-bottom: 10px;
            color: #FFF;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.title("AI For Impact")
        
        # Method 1: Using Visual Separators
        st.markdown("---")
        st.markdown("### 📚 Learning Section")
        
        with st.expander("ASSIGNMENTS", expanded=False):
            if st.button("Assignment 1", key="as1", use_container_width=True):
                st.session_state["page"] = "as1"
            if st.button("Assignment 2", key="as2", use_container_width=True):
                st.session_state["page"] = "as2"
        
        with st.expander("QUIZZES", expanded=False):
            if st.button("Quiz 1", key="quiz1", use_container_width=True):
                st.session_state["page"] = "quiz1"
            if st.button("Quiz 2", key="quiz2", use_container_width=True):
                st.session_state["page"] = "quiz2"
                
        st.markdown("---")
        st.markdown("### 🛠️ Tools Section")
        
        with st.expander("UTILITIES", expanded=False):
            if st.button("Calculator", key="calc", use_container_width=True):
                st.session_state["page"] = "calculator"
            if st.button("Converter", key="conv", use_container_width=True):
                st.session_state["page"] = "converter"
                
        st.markdown("---")
        st.markdown("### ℹ️ Help & Support")
        
        with st.expander("HELP CENTER", expanded=False):
            if st.button("FAQ", key="faq", use_container_width=True):
                st.session_state["page"] = "faq"
            if st.button("Contact", key="contact", use_container_width=True):
                st.session_state["page"] = "contact"
        
        # Method 2: Using containers (alternative approach)
        # st.markdown("## 🎓 Student Area")
        # student_section = st.container()
        # with student_section:
        #     with st.expander("MY PROGRESS", expanded=False):
        #         st.button("View Grades", key="grades", use_container_width=True)
        #         st.button("View Certificates", key="certs", use_container_width=True)
        
        # st.markdown("## 👥 Community")
        # community_section = st.container()
        # with community_section:
        #     with st.expander("DISCUSSIONS", expanded=False):
        #         st.button("Forums", key="forums", use_container_width=True)
        #         st.button("Study Groups", key="groups", use_container_width=True)

        return st.session_state.get("page", "home")
