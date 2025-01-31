import streamlit as st
import sqlite3
from database import create_tables
from theme import apply_dark_theme

def register_user(fullname, email, phone, username, password):
    """Registers a new user in the database."""
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

    cursor.execute("""
        INSERT INTO records
        (password, fullname, email, as1, as2, as3, as4, quiz1, quiz2, total)
        VALUES (?, ?, ?, 0, 0, 0, 0, 0, 0, 0)
    """, (password, fullname, email))
    conn.commit()
    conn.close()
    return True

def login_user(username, password):
    """Check if a username/password is valid."""
    conn = sqlite3.connect(st.secrets["general"]["db_path"])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    data = cursor.fetchone()
    conn.close()
    return data

def show_login_create_account():
    """Renders the login and create account tabs with updated styles."""
    apply_dark_theme()  # Apply green font & improved input styles

    tabs = st.tabs(["Login", "Create Account"])

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
                st.error("❌ Invalid username or password.")

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

                result = register_user(reg_fullname, reg_email, phone_int, reg_username, reg_password)
                if not result:
                              st.markdown('<p style="color: red; font-weight: bold;">⚠️ Username already exists. Choose a different one.</p>', unsafe_allow_html=True)
             else:
                   st.markdown('<p style="color: green; font-weight: bold;">✅ Account created successfully! You can now log in.</p>', unsafe_allow_html=True)
                
            else:
                st.error("⚠️ Please fill out all fields.")
