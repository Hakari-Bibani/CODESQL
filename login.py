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
    Sends an email with the user's password using TLS on port 587.
    """
    try:
        smtp_server = st.secrets["smtp"]["server"]
        smtp_port = st.secrets["smtp"]["port"]
        smtp_email = st.secrets["smtp"]["email"]
        smtp_password = st.secrets["smtp"]["password"]

        msg = EmailMessage()
        msg.set_content(
            f"Hi {username},\n\n"
            "We received a request to send you back your password.\n"
            f"Here is your password: {password}\n\n"
            "If you have any questions, please contact us.\n\n"
            "AI For Impact team"
        )
        msg["Subject"] = "Password Recovery"
        msg["From"] = smtp_email
        msg["To"] = recipient_email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(smtp_email, smtp_password)
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Error sending email: {e}")
        return False

def register_user(fullname, email, phone, username, password):
    """
    Registers a new user in the database with approved=0.
    """
    conn = sqlite3.connect(st.secrets["general"]["db_path"])
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM users WHERE password = ?", (password,))
    if cursor.fetchone() is not None:
        conn.close()
        return False

    try:
        cursor.execute(
            "INSERT INTO users (fullname, email, phone, username, password) VALUES (?, ?, ?, ?, ?)",
            (fullname, email, phone, username, password)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return False

    cursor.execute(
        "INSERT INTO records (password, fullname, email, as1, as2, as3, as4, quiz1, quiz2, total) VALUES (?, ?, ?, 0, 0, 0, 0, 0, 0, 0)",
        (password, fullname, email)
    )
    conn.commit()
    conn.close()
    return True

def login_user(username, password):
    """
    Validates username/password and checks if the user is approved.
    """
    conn = sqlite3.connect(st.secrets["general"]["db_path"])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        approved = user[5]
        if approved != 1:
            return "not_approved"
    return user

def show_login_create_account():
    """
    Renders the login, create account, and forgot password tabs.
    """
    apply_dark_theme()
    create_tables()

    # Custom CSS for layout adjustments
    st.markdown(
        """
        <style>
        /* Center tabs */
        .stTabs {
            display: flex;
            justify-content: center;
        }
        
        /* Reduce input width and fix eye icon */
        .stTextInput input {
            width: 50% !important;
            padding-right: 40px !important;
        }
        .stPassword input {
            width: 50% !important;
            padding-right: 40px !important;
        }
        /* Position eye icon at the end */
        button[data-testid="baseButton-header"] {
            position: absolute !important;
            right: 25% !important;
            top: 50% !important;
            transform: translateY(-50%) !important;
            background: transparent !important;
        }
        button[data-testid="baseButton-header"]:hover {
            background: transparent !important;
        }
        .stTextInput > div, .stPassword > div {
            position: relative !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Centered layout using columns
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        tabs = st.tabs(["Login", "Create Account", "Forgot Password"])

        # Login Tab
        with tabs[0]:
            st.subheader("🔑 Login")
            username = st.text_input("Username", key="login_username")
            password = st.text_input("Password", type="password", key="login_password")
            if st.button("Login"):
                user = login_user(username, password)
                if user == "not_approved":
                    st.error("Your account has not been approved yet. Please wait for admin approval.")
                elif user:
                    st.session_state["logged_in"] = True
                    st.session_state["username"] = username
                    st.success("✅ Login successful!")
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password.")

        # Create Account Tab
        with tabs[1]:
            st.subheader("🆕 Create Account")
            reg_fullname = st.text_input("Full Name", key="reg_fullname")
            reg_email = st.text_input("Email", key="reg_email")
            reg_phone = st.text_input("Mobile Number", key="reg_phone")
            reg_username = st.text_input("Username", key="reg_username")
            reg_password = st.text_input("Password", type="password", key="reg_password")
            if st.button("Register"):
                if all([reg_fullname, reg_email, reg_phone, reg_username, reg_password]):
                    try:
                        phone_int = int(reg_phone)
                        if not register_user(reg_fullname, reg_email, phone_int, reg_username, reg_password):
                            st.error("⚠️ Username or Password already exists. Choose a different one.")
                        else:
                            st.success("✅ Account created! Please wait for admin approval before logging in.")
                            push_db_to_github(st.secrets["general"]["db_path"])
                    except ValueError:
                        st.error("❌ Please enter a valid phone number (digits only).")
                else:
                    st.error("⚠️ Please fill out all fields.")

        # Forgot Password Tab
        with tabs[2]:
            st.subheader("🔒 Forgot Password")
            forgot_email = st.text_input("Enter your registered email", key="forgot_email")
            if st.button("Retrieve Password"):
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
