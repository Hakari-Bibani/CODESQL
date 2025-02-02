import streamlit as st
from theme import apply_dark_theme
from style import apply_custom_styles

def show():
    # Apply the dark theme and custom styles
    apply_dark_theme()
    apply_custom_styles()

    # Page Title with Custom Style
    st.markdown('<div class="title">🆘 Help & Support</div>', unsafe_allow_html=True)
    
    # Introduction Section
    st.write("If you need assistance, we're here to help. Please check the options below to find a solution to your problem.")

    # Instructions Section
    st.markdown(
        """
        ### How to Get Help:
        1. **Check the FAQ section below** for quick answers to common questions.
        2. **Contact your instructor** for further assistance.
        """
    )

    # FAQ Section
    st.markdown('<div class="footer">📚 Frequently Asked Questions (FAQ)</div>', unsafe_allow_html=True)

    with st.expander("Can I resubmit assignments?"):
        st.write("Yes, you can resubmit assignments until the deadline for the next assignment. After that, resubmissions for previous assignments will no longer be accepted.")

    with st.expander("Can I resubmit quizzes?"):
        st.write("No, quizzes can only be submitted once.")

    with st.expander("What if I forget my password?"):
        st.write("If you forget your password, please email [meermiro299@gmail.com](mailto:meermiro299@gmail.com) to request it.")

    # Contact Section with Custom Style
    st.markdown(
        '<div class="footer footer-partner">✉️ Need More Help? Reach out at <a href="mailto:meermiro299@gmail.com" style="color:#32CD32;">meermiro299@gmail.com</a></div>',
        unsafe_allow_html=True
    )

# Call the show function to display the interface
if __name__ == "__main__":
    show()
