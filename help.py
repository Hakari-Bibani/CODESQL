import streamlit as st

def show():
    # Enhanced custom CSS for a more polished and modern interface
    custom_css = """
    <style>
    /* General body styling */
    body {
        background-color: #f8f9fa;
        font-family: 'Inter', 'Segoe UI', system-ui, sans-serif;
        line-height: 1.6;
    }

    /* Main title styling with pale blue */
    h1 {
        font-weight: 800;
        font-size: 3rem;
        color: #a8d5ff;
        margin-bottom: 1.5rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        letter-spacing: -0.5px;
    }

    /* Subtitle and section header styling */
    h2 {
        color: #2c3e50;
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #e9ecef;
        padding-bottom: 0.5rem;
    }

    h3 {
        color: #34495e;
        font-size: 1.5rem;
        font-weight: 600;
        margin-top: 1.8rem;
        margin-bottom: 1rem;
    }

    /* Enhanced markdown text styling */
    div[data-testid="stMarkdownContainer"] p {
        font-size: 1.15rem;
        line-height: 1.8;
        color: #3a4f63;
        margin-bottom: 1rem;
    }

    /* Modern link styling */
    a {
        color: #3498db;
        text-decoration: none;
        border-bottom: 1px solid transparent;
        transition: border-bottom-color 0.2s ease;
    }

    a:hover {
        border-bottom-color: #3498db;
    }

    /* Enhanced expander styling */
    div[role="button"][aria-expanded] {
        font-size: 1.2rem;
        font-weight: 600;
        color: #2c3e50;
        background-color: #ffffff;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        transition: all 0.2s ease;
    }

    div[role="button"][aria-expanded]:hover {
        background-color: #f8f9fa;
        box-shadow: 0 4px 6px rgba(0,0,0,0.08);
    }

    /* Card styling for content sections */
    .content-section {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }

    /* List styling */
    ol {
        padding-left: 1.2rem;
        margin: 1rem 0;
    }

    ol li {
        font-size: 1.15rem;
        color: #3a4f63;
        margin-bottom: 0.8rem;
    }

    /* Expander content styling */
    .st-expander {
        background-color: #ffffff;
        border: 1px solid #e9ecef;
        border-radius: 8px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    # Page Title
    st.title("Help & Support")
    
    # Introduction Section with enhanced styling
    st.markdown("""
    <div class="content-section">
    We're here to help you succeed. Browse through our comprehensive support resources below 
    or reach out to our dedicated support team for personalized assistance.
    </div>
    """, unsafe_allow_html=True)

    # Instructions Section
    st.markdown(
        """
        ### Getting Started
        Follow these steps to find the support you need:
        1. **Browse the FAQ section** - Quick answers to common questions
        2. **Search specific topics** - Use the expandable sections below
        3. **Contact our support team** - For personalized assistance
        """
    )

    # FAQ Section with enhanced styling
    st.markdown("## Frequently Asked Questions")
    
    with st.expander("📝 Can I resubmit assignments?"):
        st.markdown("""
        Yes, you can resubmit assignments until the deadline for the next assignment. Please note:
        - Each resubmission must include all required components
        - Previous submissions will be overwritten
        - Late resubmissions are not accepted after the next assignment's deadline
        """)

    with st.expander("📊 Can I resubmit quizzes?"):
        st.markdown("""
        No, quizzes can only be submitted once. This policy ensures:
        - Fair assessment for all students
        - Accurate progress tracking
        - Consistent evaluation standards
        """)

    with st.expander("🔑 What if I forget my password?"):
        st.markdown("""
        If you need to reset your password:
        1. Email our support team at [meermiro299@gmail.com](mailto:meermiro299@gmail.com)
        2. Include your registered username/email
        3. You'll receive reset instructions within 24 hours
        """)

    # Contact Section with enhanced styling
    st.markdown(
        """
        ## Need Additional Support?
        
        <div class="content-section">
        Our support team is ready to assist you with any questions or concerns you may have.
        
        📧 Email: [meermiro299@gmail.com](mailto:meermiro299@gmail.com)
        
        **Response Time:** We typically respond within 24 hours during business days.
        </div>
        """, unsafe_allow_html=True
    )

if __name__ == "__main__":
    # Enhanced page configuration
    st.set_page_config(
        page_title="Help & Support",
        page_icon="❓",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    show()
