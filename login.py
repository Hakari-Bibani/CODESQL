def show_login_create_account():
    """
    Renders the login, create account, and forgot password tabs.
    """
    apply_dark_theme()
    create_tables()

    # Center the tabs using columns
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        tabs = st.tabs(["Login", "Create Account", "Forgot Password"])

    # ─────────────────────────
    # LOGIN TAB
    with tabs[0]:
        st.subheader("🔑 Login")
        # Add container to constrain width
        with st.container():
            c1, c2 = st.columns([1, 1])
            with c1:
                username = st.text_input("Username", key="login_username")
                password = st.text_input("Password", type="password", key="login_password")
            if st.button("Login"):
                # Existing login logic remains unchanged...

    # ─────────────────────────
    # CREATE ACCOUNT TAB
    with tabs[1]:
        st.subheader("🆕 Create Account")
        with st.container():
            c1, c2 = st.columns([1, 1])
            with c1:
                reg_fullname = st.text_input("Full Name", key="reg_fullname")
                reg_email = st.text_input("Email", key="reg_email")
                reg_phone = st.text_input("Mobile Number", key="reg_phone")
                reg_username = st.text_input("Username", key="reg_username")
                reg_password = st.text_input("Password", type="password", key="reg_password")
            # Existing registration logic remains unchanged...

    # ─────────────────────────
    # FORGOT PASSWORD TAB
    with tabs[2]:
        st.subheader("🔒 Forgot Password")
        with st.container():
            c1, c2 = st.columns([1, 1])
            with c1:
                forgot_email = st.text_input("Enter your registered email", key="forgot_email")
            # Existing password recovery logic remains unchanged...

if __name__ == '__main__':
    show_login_create_account()
