import streamlit as st

# Configure the page for an enhanced user experience
st.set_page_config(
    page_title="Help & Support",  # Browser tab title
    page_icon="❓",              # Favicon
    layout="centered",           # Centered layout
    initial_sidebar_state="auto" # Default sidebar state
)

def show() -> None:
    """
    Renders the Help & Support interface using Streamlit components.
    """
    # Page Title
    st.title("Help & Support")
    
    # Introduction Section
    st.write(
        "If you need assistance, we're here to help. "
        "Please check the options below to find a solution to your problem."
    )

    # Instructions Section
    instructions = """
    ### How to Get Help:
    1. **Check the FAQ section below** for quick answers to common questions.
    2. **Contact support** for further assistance.
    """
    st.markdown(instructions)

    # FAQ Section
    st.markdown("### Frequently Asked Questions (FAQ)")

    with st.expander("Can I resubmit assignments?"):
        st.write(
            "Yes, you can resubmit assignments until the deadline for the next assignment. "
            "After that, resubmissions for previous assignments will no longer be accepted."
        )

    with st.expander("Can I resubmit quizzes?"):
        st.write("No, quizzes can only be submitted once.")

    with st.expander("What if I forget my password?"):
        st.write(
            "If you forget your password, please email "
            "[meermiro299@gmail.com](mailto:meermiro299@gmail.com) to request assistance."
        )

    # Contact Section
    contact_info = """
    ### Need More Help?
    If you have any further questions or concerns, feel free to reach out to us via email at [meermiro299@gmail.com](mailto:meermiro299@gmail.com).
    """
    st.markdown(contact_info)

# Execute the show function to display the Help & Support page
if __name__ == "__main__":
    show()
