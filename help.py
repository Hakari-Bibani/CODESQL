import streamlit as st

def show():
    # Inject custom CSS for a polished, modern interface
    custom_css = """
    <style>
    /* General body styling */
    body {
        background-color: #f0f2f6;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    /* Title styling - Changed to pale blue */
    h1 {
        font-weight: bold;
        font-size: 2.5rem;
        color: #add8e6;  /* Pale blue color */
        margin-bottom: 1rem;
    }
    /* Subtitle and header styling */
    h3, h2 {
        color: #333333;
        margin-top: 1.5rem;
    }
    /* Yellow headers - Added new rules */
    h3:has(+ .stExpander),  /* Targets "Frequently Asked Questions" */
    h3:contains('Need More Help?') {
        color: #FFFF00 !important;  /* Yellow color */
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
    /* Expander header customization */
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

    # Page Title (now in pale blue via CSS)
    st.title("Help & Support")
    
    # Rest of your existing code remains the same...
    # ... [rest of the original code remains unchanged] ...

if __name__ == "__main__":
    st.set_page_config(page_title="Help & Support", page_icon=":question:", layout="wide")
    show()
