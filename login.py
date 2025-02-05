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
    Sends an email with the user's password to the recipient using TLS on port 587.
    Returns True if the email was sent successfully, otherwise False.
    """
    try:
        # Get SMTP configuration from st.secrets.
        smtp_server = st.secrets["smtp"]["server"]
        smtp_port = st.secrets["smtp"]["port"]
        smtp_email = st.secrets["smtp"]["email"]
        smtp_password = st.secrets["smtp"]["password"]

        # Create the email message with a polite recovery message.
        msg = EmailMessage()
        msg.set_content(
            f"Hi {username},\n\n"
            "We received a request to send you back your password.\n"
            f"Here is your password: {password}\n\n"
            "If you have any questions or need further assistance, please don't hesitate to contact us.\n\n"
            "AI For Impact team"
        )
        msg["Subject"] = "Password Recovery"
        msg["From"] = smtp_email
        msg["To"] = recipient_email

        # Connect using TLS on port 587.
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()             # Identify to the server
            server.starttls()         # Secure the connection with TLS
            server.ehlo()             # Re-identify as an encrypted connection
            server.login(smtp_email, smtp_password)
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Error sending email: {e}")
        return False

def register_user(fullname, email, phone, username, password):
    """
    Registers a new user in the database.
    Returns True on success, or False if the username or password already exists.
    Note: The user is registered with approved = 0 by default.
    """
    conn = sqlite3.connect(st.secrets["general"]["db_path"])
    cursor = conn.cursor()

    # Check if the password is already taken by another user.
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

    # Also initialize a record in the 'records' table with zeroed scores.
    cursor.execute(
        "INSERT INTO records (password, fullname, email, as1, as2, as3, as4, quiz1, quiz2, total) VALUES (?, ?, ?, 0, 0, 0, 0, 0, 0, 0)",
        (password, fullname, email)
    )
    conn.commit()
    conn.close()
    return True

def login_user(username, password):
    """
    Validates the username/password against the database.
    Returns the user row if valid and approved, otherwise:
       - returns the string "not_approved" if the user exists but is not approved,
       - returns None if credentials are invalid.
       
    Assumes the users table columns are as follows:
    (fullname, email, phone, username, password, approved)
    """
    conn = sqlite3.connect(st.secrets["general"]["db_path"])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        approved = user[5]  # Assuming the 6th column is 'approved'
        if approved != 1:
            return "not_approved"
    return user

def show_login_create_account():
    """
    Renders the login, create account, and forgot password tabs.
    Applies dark theme, ensures the database exists/updated, and then renders the three tabs.
    """
    # Apply dark theme.
    apply_dark_theme()

    # Ensure the database (and tables) exist and are up-to-date.
    create_tables()

    # Render three tabs: Login, Create Account, and Forgot Password.
    tabs = st.tabs(["Login", "Create Account", "Forgot Password"])

    # ─────────────────────────────────────────────────────────────
    # LOGIN TAB
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
                if hasattr(st, "experimental_rerun"):
                    st.experimental_rerun()
            else:
                st.error("❌ Invalid username or password.")

    # ─────────────────────────────────────────────────────────────
    # CREATE ACCOUNT TAB
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
                except ValueError:
                    st.error("❌ Please enter a valid phone number (digits only).")
                    return
                if not register_user(reg_fullname, reg_email, phone_int, reg_username, reg_password):
                    st.error("⚠️ Username or Password already exists. Choose a different one.")
                else:
                    st.success("✅ Account created successfully! Please wait for admin approval before logging in.")
                    push_db_to_github(st.secrets["general"]["db_path"])
            else:
                st.error("⚠️ Please fill out all fields.")

    # ─────────────────────────────────────────────────────────────
    # FORGOT PASSWORD TAB
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

# When this module is run, display the login/create account UI.
if __name__ == '__main__':
    show_login_create_account()
