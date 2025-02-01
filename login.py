# login.py - Manages user authentication and registration
import streamlit as st
import sqlite3
from database import create_tables
from theme import apply_dark_theme
from github_sync import push_db_to_github

def register_user(fullname, email, phone, username, password):
    """
    Registers a new user in the database. Returns True on success,
    False if username already exists (i.e., IntegrityError).
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
    Renders the login and create account tabs in dark mode.
    Pulls the existing DB (via create_tables) and pushes updates on registration.
    """
    # Apply theme first
    apply_dark_theme()

    # Ensure the database is created / pulled from GitHub
    create_tables()

    # Render two tabs: [Login] and [Create Account]
    tabs = st.tabs(["Login", "Create Account"])

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
