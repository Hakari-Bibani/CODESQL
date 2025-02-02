import streamlit as st

def show():
    # Custom CSS for professional styling
    st.markdown("""
        <style>
        /* Global Styles */
        .stApp {
            background-color: #f8fafd;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        /* Title Typography */
        .stTitle {
            font-size: 2.5rem !important;
            font-weight: 700 !important;
            color: #4a90e2 !important;  /* Pale blue color */
            letter-spacing: -0.02em !important;
            padding: 2rem 0 !important;
            border-bottom: 2px solid #e1e8f5;
            margin-bottom: 2.5rem !important;
            text-shadow: 1px 1px 2px rgba(74, 144, 226, 0.1);
        }
        
        /* Main Text Styles */
        p, li {
            font-size: 1.1rem !important;
            line-height: 1.7 !important;
            color: #2c3e50 !important;
            font-weight: 400 !important;
        }
        
        /* Section Headers */
        .section-header {
            color: #2d5b9e;
            font-size: 1.6rem;
            font-weight: 600;
            margin: 2.5rem 0 1.5rem 0;
            padding-bottom: 0.75rem;
            border-bottom: 3px solid #4a90e2;
            display: inline-block;
            letter-spacing: -0.01em;
        }
        
        /* Content Cards */
        .content-card {
            background-color: white;
            padding: 2rem;
            border-radius: 12px;
            border: 1px solid #e5eef9;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(74, 144, 226, 0.08);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        
        .content-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(74, 144, 226, 0.12);
        }
        
        /* FAQ Section */
        .streamlit-expanderHeader {
            background-color: white !important;
            border: 1px solid #d0e1f9 !important;
            border-radius: 10px !important;
            padding: 1.25rem !important;
            margin-bottom: 0.75rem !important;
            transition: all 0.2s ease-in-out !important;
            font-size: 1.1rem !important;
            font-weight: 500 !important;
            color: #2d5b9e !important;
        }
        
        .streamlit-expanderHeader:hover {
            background-color: #f5f9ff !important;
            border-color: #4a90e2 !important;
        }
        
        .streamlit-expanderContent {
            background-color: white !important;
            border: 1px solid #d0e1f9 !important;
            border-radius: 10px !important;
            padding: 1.75rem !important;
            font-size: 1.1rem !important;
            line-height: 1.7 !important;
            color: #2c3e50 !important;
        }
        
        /* Contact Section */
        .contact-section {
            background: linear-gradient(135deg, #f5f9ff 0%, #edf3fe 100%);
            padding: 2.5rem;
            border-radius: 12px;
            border: 1px solid #d0e1f9;
            margin-top: 3rem;
            box-shadow: 0 4px 6px rgba(74, 144, 226, 0.08);
        }
        
        /* Links */
        a {
            color: #4a90e2 !important;
            text-decoration: none !important;
            font-weight: 500 !important;
            transition: color 0.2s ease;
        }
        
        a:hover {
            color: #2d5b9e !important;
            text-decoration: underline !important;
        }
        
        /* List Styles */
        ol {
            padding-left: 1.5rem;
            margin: 1.25rem 0;
        }
        
        li {
            margin-bottom: 0.75rem;
            padding-left: 0.5rem;
        }
        
        strong {
            color: #2d5b9e !important;
            font-weight: 600 !important;
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
