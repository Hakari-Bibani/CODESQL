# control.py - Admin Control Panel for User Approvals
import streamlit as st
import sqlite3

def get_pending_users():
    """
    Retrieves users pending approval (approved = 0).
    Returns a list of tuples containing the rowid, fullname, email, phone, and username.
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

def main():
    st.title("Admin Control Panel")
    st.write("Approve or Reject new user accounts")
    
    # Optional: You can add an additional admin login here for extra security.
    
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
                    st.experimental_rerun()  # refresh the page after action
            with col2:
                if st.button("Reject", key=f"reject_{rowid}"):
                    update_user_approval(rowid, -1)
                    st.error(f"User {username} has been rejected.")
                    st.experimental_rerun()  # refresh the page after action
            st.markdown("---")
    else:
        st.info("No pending users for approval.")

if __name__ == '__main__':
    main()
