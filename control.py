# control.py - Admin control panel for approving/rejecting new user registrations

import streamlit as st
import sqlite3

def admin_login():
    st.sidebar.header("Admin Login")
    admin_username = st.sidebar.text_input("Username")
    admin_password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login as Admin"):
        conn = sqlite3.connect(st.secrets["general"]["db_path"])
        cursor = conn.cursor()
        # Assuming you have an 'admin' table with admin credentials
        cursor.execute("SELECT * FROM admin WHERE username=? AND password=?", (admin_username, admin_password))
        admin = cursor.fetchone()
        conn.close()
        if admin:
            st.session_state["admin_logged_in"] = True
            st.success("Admin logged in.")
        else:
            st.error("Invalid admin credentials.")

def get_pending_users():
    """
    Retrieves all users whose approved status is 0 (pending).
    """
    conn = sqlite3.connect(st.secrets["general"]["db_path"])
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, fullname, email, username FROM users WHERE approved=0")
    pending = cursor.fetchall()
    conn.close()
    return pending

def update_user_status(user_id, status):
    """
    Updates a user's approved status.
      - 1 for approved
      - -1 for rejected
    """
    conn = sqlite3.connect(st.secrets["general"]["db_path"])
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET approved=? WHERE rowid=?", (status, user_id))
    conn.commit()
    conn.close()

def admin_panel():
    st.header("Admin Panel: Manage User Approvals")
    pending = get_pending_users()
    if not pending:
        st.info("No pending user registrations.")
    else:
        for user in pending:
            user_id, fullname, email, username = user
            st.write(f"**User ID:** {user_id} | **Name:** {fullname} | **Email:** {email} | **Username:** {username}")
            col1, col2 = st.columns(2)
            if col1.button(f"Approve {username}", key=f"approve_{user_id}"):
                update_user_status(user_id, 1)
                st.success(f"User {username} approved.")
                st.experimental_rerun()  # Refresh the page to update the list
            if col2.button(f"Reject {username}", key=f"reject_{user_id}"):
                update_user_status(user_id, -1)
                st.error(f"User {username} rejected.")
                st.experimental_rerun()

def main():
    if "admin_logged_in" not in st.session_state:
        st.session_state["admin_logged_in"] = False

    if not st.session_state["admin_logged_in"]:
        admin_login()
    else:
        admin_panel()

if __name__ == "__main__":
    main()
