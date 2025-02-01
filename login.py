# login.py
import streamlit as st
import sqlite3
from database import create_tables
from theme import apply_dark_theme
from github_sync import push_db_to_github, pull_db_from_github

def register_user(fullname, email, phone, username, password):
    """Registers a new user in the database (no password hashing for simplicity)."""
    # 1) Pull the latest DB to ensure we have the most up-to-date data
    pull_db_from_github(st.secrets["general"]["db_path"])

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

    # Insert a default record as well
    cursor.execute("""
        INSERT INTO records
        (password, fullname, email, as1, as2, as3, as4, quiz1, quiz2, total)
        VALUES (?, ?, ?, 0, 0, 0, 0, 0, 0, 0)
    """, (password, fullname, email))
    conn.commit()
    conn.close()

    # 2) Push the updated DB so new user is saved remotely
    push_db_to_github(st.secrets["general"]["db_path"])
    
    return True

def login_user(username, password):
    """Check if a username/password is valid in the database."""
    # Pull the latest DB to reflect any recent changes
    pull_db_from_github(st.secrets["general"]["db_path"])
    
    conn = sqlite3.connect(st.secrets["general"]["db_path"])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    data = cursor.fetchone()
    conn.close()
    return data

def show_login_create_account():
    """Renders the login and create account tabs with dark theme + DB sync."""
    apply_dark_theme()
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
                st.markdown('<p class="error-text">❌ Invalid username or password.</p>', unsafe_allow_html=True)
    
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
                    st.markdown('<p class="error-text">❌ Please enter a valid phone number (digits only).</p>', unsafe_allow_html=True)
                    return
                result = register_user(reg_fullname, reg_email, phone_int, reg_username, reg_password)
                if not result:
                    st.markdown('<p class="error-text">⚠️ Username already exists. Choose a different one.</p>', unsafe_allow_html=True)
                else:
                    st.success("✅ Account created successfully! You can now log in.")
            else:
                st.markdown('<p class="error-text">⚠️ Please fill out all fields.</p>', unsafe_allow_html=True)
