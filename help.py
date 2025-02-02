import streamlit as st

def show():
    # Custom CSS for better styling
    st.markdown("""
        <style>
        .stTitle {
            font-size: 2.5rem !important;
            padding-bottom: 2rem !important;
            color: #1E3D59 !important;
        }
        .section-header {
            color: #1E3D59;
            font-size: 1.5rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }
        .help-card {
            background-color: #f8f9fa;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 1.5rem;
        }
        .contact-box {
            background-color: #E8F4F9;
            padding: 2rem;
            border-radius: 10px;
            margin-top: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Page Title with custom styling
    st.title("Help & Support")
    
    # Introduction Section with card styling
    with st.container():
        st.markdown('<div class="help-card">', unsafe_allow_html=True)
        st.write("If you need assistance, we're here to help. Please check the options below to find a solution to your problem.")
        st.markdown('</div>', unsafe_allow_html=True)

    # Instructions Section
    st.markdown('<p class="section-header">How to Get Help:</p>', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="help-card">', unsafe_allow_html=True)
        st.markdown("""
        1. **Check the FAQ section below** for quick answers to common questions.
        2. **Contact support** for further assistance.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    # FAQ Section with improved expander styling
    st.markdown('<p class="section-header">Frequently Asked Questions (FAQ)</p>', unsafe_allow_html=True)
    
    # Custom CSS for FAQ expanders
    st.markdown("""
        <style>
        .streamlit-expanderHeader {
            background-color: #f8f9fa;
            border-radius: 5px;
            margin-bottom: 0.5rem;
        }
        .streamlit-expanderContent {
            background-color: white;
            border-radius: 0 0 5px 5px;
            padding: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.expander("Can I resubmit assignments?"):
        st.write("Yes, you can resubmit assignments until the deadline for the next assignment. After that, resubmissions for previous assignments will no longer be accepted.")
    
    with st.expander("Can I resubmit quizzes?"):
        st.write("No, quizzes can only be submitted once.")
    
    with st.expander("What if I forget my password?"):
        st.write("If you forget your password, please email [meermiro299@gmail.com](mailto:meermiro299@gmail.com) to request assistance.")

    # Contact Section with special styling
    st.markdown('<div class="contact-box">', unsafe_allow_html=True)
    st.markdown('<p class="section-header">Need More Help?</p>', unsafe_allow_html=True)
    st.markdown("""
        If you have any further questions or concerns, feel free to reach out to us via email at [meermiro299@gmail.com](mailto:meermiro299@gmail.com).
    """)
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    show()
