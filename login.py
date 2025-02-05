def show_login_create_account():
    """
    Renders the login, create account, and forgot password tabs.
    """
    apply_dark_theme()
    create_tables()  # Ensure database and tables exist

    # Center the tabs using a 3-column layout
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        tabs = st.tabs(["Login", "Create Account", "Forgot Password"])

    # ─────────────────────────
    # LOGIN TAB
    with tabs[0]:
        st.subheader("🔑 Login")
        with st.container():
            # Create two columns for input fields
            c1, c2 = st.columns([1, 1])
            with c1:
                username = st.text_input("Username", key="login_username")
                password = st.text_input("Password", type="password", key="login_password")
        
        # Login button remains full width but centered
        if st.button("Login", key="login_btn"):
            user = login_user(username, password)
            if user == "not_approved":
                st.error("Your account has not been approved yet. Please wait for admin approval.")
            elif user:
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.success("✅ Login successful!")
                if hasattr(st, "experimental_rerun"):
                    st.experimental_rerun()
            else:
                st.error("❌ Invalid username or password.")

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

        # Registration button
        if st.button("Register", key="reg_btn"):
            if all([reg_fullname, reg_email, reg_phone, reg_username, reg_password]):
                try:
                    phone_int = int(reg_phone)
                except ValueError:
                    st.error("❌ Please enter a valid phone number (digits only).")
                    return
                if not register_user(reg_fullname, reg_email, phone_int, reg_username, reg_password):
                    st.error("⚠️ Username or Password already exists. Choose a different one.")
                else:
                    st.success("✅ Account created! Please wait for admin approval before logging in.")
                    push_db_to_github(st.secrets["general"]["db_path"])
            else:
                st.error("⚠️ Please fill out all fields.")

    # ─────────────────────────
    # FORGOT PASSWORD TAB
    with tabs[2]:
        st.subheader("🔒 Forgot Password")
        with st.container():
            c1, c2 = st.columns([1, 1])
            with c1:
                forgot_email = st.text_input("Enter your registered email", key="forgot_email")

        # Password recovery button
        if st.button("Retrieve Password", key="pwd_btn"):
            if not forgot_email:
                st.error("Please enter an email address.")
            else:
                conn = sqlite3.connect(st.secrets["general"]["db_path"])
                cursor = conn.cursor()
                cursor.execute("SELECT username, password FROM users WHERE email=?", (forgot_email,))
                result = cursor.fetchone()
                conn.close()

                if result:
                    username, password = result
                    if send_password_email(forgot_email, username, password):
                        st.success("Your password has been sent to your email address.")
                    else:
                        st.error("Failed to send email. Please try again later.")
                else:
                    st.error("This email is not registered in our system.")

if __name__ == '__main__':
    show_login_create_account()
