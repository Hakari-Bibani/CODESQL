# login.py - Manages user authentication, registration, and password recovery
import streamlit as st
import sqlite3
import smtplib
from email.message import EmailMessage
from database import create_tables
from theme import apply_dark_theme
from github_sync import push_db_to_github

def send_password_email(recipient_email, username, password):
    """
    Sends an email with the user's password to the recipient.
    Returns True if the email was sent successfully, otherwise False.
    """
    try:
        # Get SMTP configuration from secrets
        smtp_server = st.secrets["smtp"]["server"]
        smtp_port = st.secrets["smtp"]["port"]
        smtp_username = st.secrets["smtp"]["username"]
        smtp_password = st.secrets["smtp"]["password"]

        # Create the email message
        msg = EmailMessage()
        msg.set_content(
            f"Hi {username},\n\n"
            "We received a request to send you back your password.\n"
            f"Here is your password: {password}\n\n"
            "If you have any questions or need further assistance, please don't hesitate to contact us.\n\n"
            "AI For Impact team"
        )
        msg["Subject"] = "Password Recovery"
        msg["From"] = smtp_username
        msg["To"] = recipient_email

        # Send the email using a secure SSL connection
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Error sending email: {e}")
        return False

def register_user(fullname, email, phone, username, password):
    """
    Registers a new user in the database. Returns True on success,
    False if the username already exists (i.e., IntegrityError).
    """
    conn = sqlite3.connect(st.secrets["general"]["db_path"])
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (fullname, email, phone, username, password) VALUES (?, ?, ?, ?, ?)",
            (fullname, email, phone, username, password)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return False

    # Also initialize a record in the 'records' table with zeroed scores
    cursor.execute("""
        INSERT INTO records
        (password, fullname, email, as1, as2, as3, as4, quiz1, quiz2, total)
        VALUES (?, ?, ?, 0, 0, 0, 0, 0, 0, 0)
    """, (password, fullname, email))
    conn.commit()
    conn.close()
    return True

def login_user(username, password):
    """
    Validates username/password in the database. Returns row data if valid,
    otherwise None.
    """
    conn = sqlite3.connect(st.secrets["general"]["db_path"])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    data = cursor.fetchone()
    conn.close()
    return data

def show_login_create_account():
    """
    Renders the login, create account, and forgot password tabs in dark mode.
    Ensures the database is created/pulled from GitHub.
    """
    # Apply the dark theme
    apply_dark_theme()

    # Ensure the database is created / updated
    create_tables()

    # Render three tabs: [Login], [Create Account], [Forgot Password]
    tabs = st.tabs(["Login", "Create Account", "Forgot Password"])

    # ─────────────────────────────────────────────────────────────────
    # LOGIN TAB
    # ─────────────────────────────────────────────────────────────────
    with tabs[0]:
        st.subheader("🔑 Login")

        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login"):
            user = login_user(username, password)
            if user:
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.success("✅ Login successful!")
                st.rerun()
            else:
                st.markdown(
                    '<p class="error-text">❌ Invalid username or password.</p>',
                    unsafe_allow_html=True
                )

    # ─────────────────────────────────────────────────────────────────
    # CREATE ACCOUNT TAB
    # ─────────────────────────────────────────────────────────────────
    with tabs[1]:
        st.subheader("🆕 Create Account")

        reg_fullname = st.text_input("Full Name", key="reg_fullname")
        reg_email = st.text_input("Email", key="reg_email")
        reg_phone = st.text_input("Mobile Number", key="reg_phone")
        reg_username = st.text_input("Username", key="reg_username")
        reg_password = st.text_input("Password", type="password", key="reg_password")

        if st.button("Register"):
            # Check if all fields are filled
            if all([reg_fullname, reg_email, reg_phone, reg_username, reg_password]):
                # Validate phone number is digits only
                try:
                    phone_int = int(reg_phone)
                except ValueError:
                    st.markdown(
                        '<p class="error-text">❌ Please enter a valid phone number (digits only).</p>',
                        unsafe_allow_html=True
                    )
                    return

                # Attempt registration
                result = register_user(reg_fullname, reg_email, phone_int, reg_username, reg_password)
                if not result:
                    # Username conflict
                    st.markdown(
                        '<p class="error-text">⚠️ Username already exists. Choose a different one.</p>',
                        unsafe_allow_html=True
                    )
                else:
                    # Success, push DB to GitHub
                    st.success("✅ Account created successfully! You can now log in.")
                    push_db_to_github(st.secrets["general"]["db_path"])
            else:
                st.markdown(
                    '<p class="error-text">⚠️ Please fill out all fields.</p>',
                    unsafe_allow_html=True
                )

    # ─────────────────────────────────────────────────────────────────
    # FORGOT PASSWORD TAB
    # ─────────────────────────────────────────────────────────────────
    with tabs[2]:
        st.subheader("🔒 Forgot Password")

        forgot_email = st.text_input("Enter your registered email", key="forgot_email")
        if st.button("Retrieve Password"):
            if forgot_email:
                conn = sqlite3.connect(st.secrets["general"]["db_path"])
                cursor = conn.cursor()
                cursor.execute("SELECT username, password FROM users WHERE email=?", (forgot_email,))
                user_data = cursor.fetchone()
                conn.close()

                if user_data:
                    username, password = user_data
                    if send_password_email(forgot_email, username, password):
                        st.success("Your password has been sent to your email address.")
                    else:
                        st.error("Failed to send email. Please try again later.")
                else:
                    st.error("This email is not registered in our system.")
            else:
                st.error("Please enter an email address.")
