import streamlit as st

# Set the page configuration for a wider, more modern layout
st.set_page_config(page_title="Help & Support", page_icon=":question:", layout="wide")

# Inject custom CSS for a polished, modern interface
custom_css = """
<style>
/* General body styling */
body {
    background-color: #f0f2f6;
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}

/* Title styling */
h1 {
    font-weight: bold;
    font-size: 2.5rem;
    color: #333333;
    margin-bottom: 1rem;
}

/* Subtitle and header styling */
h3, h2 {
    color: #333333;
    margin-top: 1.5rem;
}

/* Markdown text styling */
div[data-testid="stMarkdownContainer"] p {
    font-size: 1.1rem;
    line-height: 1.6;
}

/* Link styling */
a {
    color: #4a90e2;
    text-decoration: none;
}

/* Expander customization */
div[role="button"][aria-expanded] {
    font-size: 1.1rem;
    font-weight: bold;
}
div[role="button"][aria-expanded]::after {
    font-size: 1rem;
    margin-left: 0.5rem;
}

/* Card-like styling for expanders */
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

def show():
    # Page Title
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

    # FAQ Section
    st.markdown("### Frequently Asked Questions (FAQ)")
    
    with st.expander("Can I resubmit assignments?"):
        st.write("Yes, you can resubmit assignments until the deadline for the next assignment. After that, resubmissions for previous assignments will no longer be accepted.")

    with st.expander("Can I resubmit quizzes?"):
        st.write("No, quizzes can only be submitted once.")

    with st.expander("What if I forget my password?"):
        st.write("If you forget your password, please email [meermiro299@gmail.com](mailto:meermiro299@gmail.com) to request assistance.")

    # Contact Section
    st.markdown(
        """
        ### Need More Help?
        If you have any further questions or concerns, feel free to reach out to us via email at [meermiro299@gmail.com](mailto:meermiro299@gmail.com).
        """
    )

if __name__ == "__main__":
    show()
