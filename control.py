# control.py - Admin Control Panel for User Approvals
import streamlit as st
import sqlite3
from github_sync import push_db_to_github  # This should use st.secrets["general"]["repo"] and st.secrets["general"]["token"]

def admin_login():
    """
    Displays an admin login form and returns True if the entered credentials are correct.
    """
    st.subheader("Admin Login")
    admin_username = st.text_input("Admin Username", key="admin_username")
    admin_password = st.text_input("Admin Password", type="password", key="admin_password")
    if st.button("Login as Admin"):
        if (admin_username == st.secrets["admin"]["username"] and 
            admin_password == st.secrets["admin"]["password"]):
            st.session_state["admin_logged_in"] = True
            st.success("Admin login successful!")
        else:
            st.error("Invalid admin credentials.")

def get_pending_users():
    """
    Retrieves users pending approval (approved = 0).
    Returns a list of tuples: (rowid, fullname, email, phone, username).
    """
    conn = sqlite3.connect(st.secrets["general"]["db_path"])
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, fullname, email, phone, username FROM users WHERE approved = 0")
    pending = cursor.fetchall()
    conn.close()
    return pending

def update_user_approval(rowid, new_status):
    """
    Updates the 'approved' field for the user with the given rowid.
    new_status should be 1 (approve) or -1 (reject).
    """
    conn = sqlite3.connect(st.secrets["general"]["db_path"])
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET approved = ? WHERE rowid = ?", (new_status, rowid))
    conn.commit()
    conn.close()
    # After updating the database, push the changes to GitHub.
    push_db_to_github(st.secrets["general"]["db_path"])

def show_admin_panel():
    """
    Displays the admin control panel for approving or rejecting user accounts.
    """
    st.title("Admin Control Panel")
    st.write("Approve or Reject new user accounts")

    pending_users = get_pending_users()
    if pending_users:
        for user in pending_users:
            rowid, fullname, email, phone, username = user
            st.markdown(f"**Name:** {fullname} (*{username}*)")
            st.markdown(f"**Email:** {email}")
            st.markdown(f"**Phone:** {phone}")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Approve", key=f"approve_{rowid}"):
                    update_user_approval(rowid, 1)
                    st.success(f"User {username} has been approved.")
                    st.experimental_rerun()
            with col2:
                if st.button("Reject", key=f"reject_{rowid}"):
                    update_user_approval(rowid, -1)
                    st.error(f"User {username} has been rejected.")
                    st.experimental_rerun()
            st.markdown("---")
    else:
        st.info("No pending users for approval.")

def main():
    # Check if admin is logged in; if not, show login form.
    if "admin_logged_in" not in st.session_state or not st.session_state["admin_logged_in"]:
        admin_login()
    else:
        show_admin_panel()

if __name__ == '__main__':
    main()
