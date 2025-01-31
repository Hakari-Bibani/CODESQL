''' theme.py - Manages dark mode styles '''
import streamlit as st

def apply_dark_theme():
    st.markdown("""
        <style>
        body {
            background-color: #121212;
            color: #ffffff;
        }
        .title {
            color: #ff4757;
            font-size: 2.5rem;
            font-weight: bold;
            text-align: center;
            animation: move 2s infinite;
            margin-bottom: 1rem;
        }
        @keyframes move {
            0% { transform: translateX(0); }
            50% { transform: translateX(10px); }
            100% { transform: translateX(0); }
        }
        .footer {
            text-align: center;
            font-size: 1.2rem;
            color: #bdc3c7;
            margin-top: 2rem;
        }
        .stTextInput > label, .stButton > button, .stSelectbox > label {
            color: white !important;
        }
        .stTextInput, .stSelectbox, .stButton > button {
            background-color: #1e1e1e !important;
            color: white !important;
            border-radius: 5px;
            border: 1px solid #444;
        }
        .stButton > button:hover {
            background-color: #ff4757 !important;
        }
        </style>
    """, unsafe_allow_html=True)

''' login.py - Manages authentication with dark theme '''
import streamlit as st
from database import create_tables
from theme import apply_dark_theme
import sqlite3

def register_user(fullname, email, phone, username, password):
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
    conn = sqlite3.connect(st.secrets["general"]["db_path"])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    data = cursor.fetchone()
    conn.close()
    return data

def show_login_create_account():
    apply_dark_theme()
    tabs = st.tabs(["Login", "Create Account"])
    with tabs[0]:
        st.subheader("Login")
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")
        if st.button("Login"):
            user = login_user(username, password)
            if user:
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid username or password.")

    with tabs[1]:
        st.subheader("Create Account")
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
                    st.error("Please enter a valid phone number (digits only).")
                    return
                result = register_user(reg_fullname, reg_email, phone_int, reg_username, reg_password)
                if not result:
                    st.error("Username already exists. Please choose a different one.")
                else:
                    st.success("Account created successfully! You can now log in.")
