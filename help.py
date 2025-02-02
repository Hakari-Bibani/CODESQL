import streamlit as st

def show():
    custom_css = """
    <style>
    /* General body styling */
    body {
        background-color: #f0f2f6;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    /* Pale blue title */
    h1 {
        color: #add8e6 !important;
        font-weight: bold;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    /* Yellow headers */
    h3:contains('Frequently Asked Questions'), 
    h3:contains('Need More Help?') {
        color: #FFFF00 !important;
    }
    /* Rest of original styles */
    div[data-testid="stMarkdownContainer"] p {
        font-size: 1.1rem;
        line-height: 1.6;
    }
    a {
        color: #4a90e2;
        text-decoration: none;
    }
    .st-expander {
        background-color: #ffffff;
        border: 1px solid #d1d1d1;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    # Page Title (now pale blue)
    st.title("Help & Support")
    
    # Introduction Section
    st.write("If you need assistance, we're here to help. Please check the options below to find a solution to your problem.")

    # Instructions Section
    st.markdown(
        """
        ### How to Get Help:
        1. **Check the FAQ section below** for quick answers to common questions.
        2. **Contact support** for further assistance.
        """
    )

    # FAQ Section with yellow header
    st.markdown("### Frequently Asked Questions (FAQ)")
    
    with st.expander("Can I resubmit assignments?"):
        st.write("Yes, you can resubmit assignments until the deadline for the next assignment. After that, resubmissions for previous assignments will no longer be accepted.")

    with st.expander("Can I resubmit quizzes?"):
        st.write("No, quizzes can only be submitted once.")

    with st.expander("What if I forget my password?"):
        st.write("If you forget your password, please email [meermiro299@gmail.com](mailto:meermiro299@gmail.com) to request assistance.")

    # Contact Section with yellow header
    st.markdown(
        """
        ### Need More Help?
        If you have any further questions or concerns, feel free to reach out to us via email at [meermiro299@gmail.com](mailto:meermiro299@gmail.com).
        """
    )

if __name__ == "__main__":
    st.set_page_config(page_title="Help & Support", page_icon=":question:", layout="wide")
    show()
