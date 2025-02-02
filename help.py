import streamlit as st

def show():
    # Custom CSS for professional styling
    st.markdown("""
        <style>
        /* Global Styles */
        .stApp {
            background-color: #f7f9fc;
        }
        
        /* Typography */
        .stTitle {
            font-size: 2.2rem !important;
            font-weight: 600 !important;
            color: #1a2b4e !important;
            letter-spacing: -0.5px !important;
            padding: 1.5rem 0 !important;
            border-bottom: 1px solid #e1e5eb;
            margin-bottom: 2rem !important;
        }
        
        /* Section Headers */
        .section-header {
            color: #1a2b4e;
            font-size: 1.4rem;
            font-weight: 500;
            margin: 2rem 0 1rem 0;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #3b82f6;
            display: inline-block;
        }
        
        /* Content Cards */
        .content-card {
            background-color: white;
            padding: 1.8rem;
            border-radius: 8px;
            border: 1px solid #e5e7eb;
            margin-bottom: 1.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }
        
        /* FAQ Section */
        .streamlit-expanderHeader {
            background-color: white !important;
            border: 1px solid #e5e7eb !important;
            border-radius: 6px !important;
            padding: 1rem !important;
            margin-bottom: 0.5rem !important;
            transition: all 0.2s ease-in-out !important;
        }
        
        .streamlit-expanderHeader:hover {
            background-color: #f8fafc !important;
            border-color: #3b82f6 !important;
        }
        
        .streamlit-expanderContent {
            background-color: white !important;
            border: 1px solid #e5e7eb !important;
            border-top: none !important;
            border-radius: 0 0 6px 6px !important;
            padding: 1.5rem !important;
        }
        
        /* Contact Section */
        .contact-section {
            background: linear-gradient(to right, #f8fafc, #f1f5f9);
            padding: 2rem;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
            margin-top: 2.5rem;
        }
        
        /* Links */
        a {
            color: #3b82f6 !important;
            text-decoration: none !important;
        }
        
        a:hover {
            text-decoration: underline !important;
        }
        
        /* List Styles */
        ol {
            padding-left: 1.2rem;
            margin: 1rem 0;
        }
        
        li {
            margin-bottom: 0.5rem;
            line-height: 1.6;
        }
        </style>
    """, unsafe_allow_html=True)

    # Page Title
    st.title("Help & Support")
    
    # Introduction Section
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.write("If you need assistance, we're here to help. Please check the options below to find a solution to your problem.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Instructions Section
    st.markdown('<p class="section-header">How to Get Help</p>', unsafe_allow_html=True)
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown("""
    1. **Check the FAQ section below** for quick answers to common questions.
    2. **Contact support** for further assistance.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # FAQ Section
    st.markdown('<p class="section-header">Frequently Asked Questions</p>', unsafe_allow_html=True)
    
    # FAQ Items with improved styling
    for question, answer in [
        ("Can I resubmit assignments?", 
         "Yes, you can resubmit assignments until the deadline for the next assignment. After that, resubmissions for previous assignments will no longer be accepted."),
        ("Can I resubmit quizzes?", 
         "No, quizzes can only be submitted once."),
        ("What if I forget my password?", 
         "If you forget your password, please email [meermiro299@gmail.com](mailto:meermiro299@gmail.com) to request assistance.")
    ]:
        with st.expander(question):
            st.markdown(answer)

    # Contact Section
    st.markdown('<div class="contact-section">', unsafe_allow_html=True)
    st.markdown('<p class="section-header">Need More Help?</p>', unsafe_allow_html=True)
    st.markdown("""
        If you have any further questions or concerns, feel free to reach out to us via email at [meermiro299@gmail.com](mailto:meermiro299@gmail.com).
    """)
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    show()
