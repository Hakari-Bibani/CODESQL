# control.py - Enhanced Admin Control Panel
import streamlit as st
import sqlite3
import hashlib
from datetime import datetime
from github_sync import push_db_to_github

# Database Configuration
DB_PATH = st.secrets["general"]["db_path"]
INIT_SCRIPTS = [
    """CREATE TABLE IF NOT EXISTS users (
        rowid INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT,
        username TEXT UNIQUE NOT NULL,
        approved INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""",
    """CREATE TABLE IF NOT EXISTS audit_log (
        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        action TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        admin_user TEXT NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(rowid)
    )"""
]

# Security Functions
def _hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def _init_db():
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH, timeout=20)
        cursor = conn.cursor()
        for script in INIT_SCRIPTS:
            cursor.execute(script)
        conn.commit()
    except sqlite3.Error as e:
        st.error(f"Database initialization failed: {str(e)}")
    finally:
        if conn: conn.close()

# Database Operations
@st.cache_resource
def get_db_connection():
    return sqlite3.connect(DB_PATH, timeout=10)

def get_pending_users():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT rowid, fullname, email, phone, username, created_at 
                       FROM users WHERE approved = 0 ORDER BY created_at DESC""")
        return cursor.fetchall()
    except sqlite3.Error as e:
        st.error(f"Database error: {str(e)}")
        return []

def update_user_batch(actions, admin_user):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        for rowid, action in actions:
            status = 1 if action == 'approve' else -1
            cursor.execute("UPDATE users SET approved = ? WHERE rowid = ?", (status, rowid))
            cursor.execute("""INSERT INTO audit_log (user_id, action, admin_user) 
                           VALUES (?, ?, ?)""", (rowid, action.upper(), admin_user))
        
        conn.commit()
        push_db_to_github(DB_PATH)  # Sync after batch
        return True
    except sqlite3.Error as e:
        st.error(f"Batch update failed: {str(e)}")
        conn.rollback()
        return False

def get_audit_logs():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT u.username, a.action, a.timestamp, a.admin_user 
                       FROM audit_log a JOIN users u ON a.user_id = u.rowid 
                       ORDER BY a.timestamp DESC LIMIT 100""")
        return cursor.fetchall()
    except sqlite3.Error as e:
        st.error(f"Audit log error: {str(e)}")
        return []

# UI Components
def admin_login():
    with st.container():
        st.subheader("Admin Authentication 🔒")
        admin_username = st.text_input("Admin Username", key="admin_user")
        admin_password = st.text_input("Password", type="password", key="admin_pass")
        
        if st.button("Authenticate"):
            if (admin_username == st.secrets["admin"]["username"] and 
                _hash_password(admin_password) == st.secrets["admin"]["password_hash"]):
                st.session_state.update({
                    "admin_logged_in": True,
                    "admin_user": admin_username
                })
                st.rerun()
            else:
                st.error("Invalid credentials")

def user_management_section():
    st.header("Pending User Approvals 📋")
    pending_users = get_pending_users()
    
    if not pending_users:
        st.info("No pending approvals")
        return

    selected_users = []
    with st.form("batch_actions"):
        for user in pending_users:
            rowid, fullname, email, phone, username, created = user
            with st.expander(f"{fullname} ({username})"):
                cols = st.columns([3,1])
                cols[0].markdown(f"""
                - **Email:** `{email}`  
                - **Phone:** `{phone}`  
                - **Registered:** `{created.split('.')[0]}`
                """)
                selected = cols[1].checkbox("Select", key=f"check_{rowid}")
                if selected:
                    selected_users.append(rowid)
        
        batch_cols = st.columns([1,1,3])
        if batch_cols[0].form_submit_button("✅ Approve Selected"):
            process_batch_actions(selected_users, 'approve')
        if batch_cols[1].form_submit_button("❌ Reject Selected"):
            process_batch_actions(selected_users, 'reject')

def audit_log_section():
    with st.expander("Audit Logs 📜", expanded=True):
        logs = get_audit_logs()
        if not logs:
            st.info("No audit records")
            return
            
        for log in logs:
            username, action, timestamp, admin = log
            status = "✅" if action == 'APPROVE' else "❌"
            st.markdown(f"""
            **{status} {action.title()}** - {username}  
            *By {admin} at {timestamp.split('.')[0]}*
            """)

def process_batch_actions(user_ids, action):
    if not user_ids:
        st.warning("No users selected!")
        return
        
    actions = [(uid, action) for uid in user_ids]
    if update_user_batch(actions, st.session_state.admin_user):
        st.success(f"{action.title()}d {len(user_ids)} users")
        st.cache_resource.clear()
        st.rerun()

# Main Layout
def main_panel():
    _init_db()
    
    st.title("Admin Control Panel 🛠️")
    st.sidebar.header("Admin Tools")
    if st.sidebar.button("🚪 Logout"):
        st.session_state.clear()
        st.rerun()
    
    user_management_section()
    audit_log_section()

# App Flow
def main():
    if not st.session_state.get("admin_logged_in"):
        admin_login()
    else:
        main_panel()

if __name__ == "__main__":
    st.set_page_config(page_title="Admin Control", layout="wide")
    main()
