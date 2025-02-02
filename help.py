import streamlit as st

def show():
    custom_css = """
    <style>
    /* Pale blue title */
    h1 {
        color: #add8e6 !important;
        font-weight: bold;
        font-size: 2.5rem;
    }
    
    /* Orange header styling */
    .orange-header {
        color: #FFA500 !important;
        margin-top: 1.5rem;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    # Page Title
    st.title("Help & Support")

    # FAQ Section with orange header
    st.markdown(
        '<h3 class="orange-header">Frequently Asked Questions (FAQ)</h3>', 
        unsafe_allow_html=True
    )
    
    with st.expander("Can I resubmit assignments?"):
        st.write("Yes, you can resubmit assignments until the deadline...")

    # Rest of your FAQ expanders...

    # Contact Section with orange header
    st.markdown(
        '<h3 class="orange-header">Need More Help?</h3>', 
        unsafe_allow_html=True
    )
    st.markdown("If you have any further questions...")

if __name__ == "__main__":
    st.set_page_config(page_title="Help & Support", page_icon=":question:", layout="wide")
    show()
