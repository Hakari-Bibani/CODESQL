# admin.py - Admin dashboard for managing the app’s data
import streamlit as st
import sqlite3
from database import create_tables
from github_sync import push_db_to_github

def admin_login(username, password):
    """
    Authenticate an admin user based on credentials stored in the admin table.
    """
    conn = sqlite3.connect(st.secrets["general"]["db_path"])
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM admin WHERE username=? AND password=?", 
        (username, password)
    )
    admin_user = cursor.fetchone()
    conn.close()
    return admin_user

def view_users():
    """
    Fetch all registered users from the users table.
    """
    conn = sqlite3.connect(st.secrets["general"]["db_path"])
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, fullname, email, phone, username FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

def delete_user(user_id):
    """
    Delete a user from the users table by rowid.
    """
    conn = sqlite3.connect(st.secrets["general"]["db_path"])
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE rowid=?", (user_id,))
    conn.commit()
    conn.close()

def view_records():
    """
    Fetch all records from the records table.
    """
    conn = sqlite3.connect(st.secrets["general"]["db_path"])
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, * FROM records")
    records = cursor.fetchall()
    conn.close()
    return records

def main():
    st.title("Admin Dashboard")
    
    # Ensure the database and required tables are created
    create_tables()

    # Check for admin login status
    if "admin_logged_in" not in st.session_state:
        st.session_state["admin_logged_in"] = False

    if not st.session_state["admin_logged_in"]:
        st.subheader("Admin Login")
        admin_username = st.text_input("Admin Username")
        admin_password = st.text_input("Admin Password", type="password")
        if st.button("Login"):
            if admin_login(admin_username, admin_password):
                st.session_state["admin_logged_in"] = True
                st.success("Admin login successful!")
            else:
                st.error("Invalid admin credentials")
        return  # Stop further rendering until logged in

    # Once logged in, provide a sidebar with different admin options
    st.sidebar.title("Admin Options")
    option = st.sidebar.radio("Select an option", ("View Users", "View Records", "Database Operations"))

    if option == "View Users":
        st.header("Registered Users")
        users = view_users()
        if users:
            for user in users:
                st.write(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Phone: {user[3]}, Username: {user[4]}")
                if st.button("Delete User", key=f"delete_{user[0]}"):
                    delete_user(user[0])
                    st.success(f"User {user[4]} deleted.")
                    # Push changes to GitHub after deletion
                    push_db_to_github(st.secrets["general"]["db_path"])
                    st.experimental_rerun()
        else:
            st.info("No users found.")

    elif option == "View Records":
        st.header("User Records")
        records = view_records()
        if records:
            for record in records:
                st.write(record)
        else:
            st.info("No records found.")

    elif option == "Database Operations":
        st.header("Database Operations")
        st.write("**Warning:** These operations can modify your database schema. Proceed with caution!")
        operation = st.selectbox("Operation", ["Add Column", "Delete Column", "Execute Custom SQL"])
        table = st.text_input("Table Name", value="users")
        column_name = st.text_input("Column Name")
        data_type = st.text_input("Data Type (for Add Column)", value="TEXT")
        custom_sql = st.text_area("Custom SQL (if needed)")
        
        if st.button("Execute Operation"):
            conn = sqlite3.connect(st.secrets["general"]["db_path"])
            cursor = conn.cursor()
            try:
                if operation == "Add Column":
                    sql = f"ALTER TABLE {table} ADD COLUMN {column_name} {data_type}"
                    cursor.execute(sql)
                    st.success(f"Column '{column_name}' added to {table}.")
                elif operation == "Delete Column":
                    st.error("SQLite does not support DROP COLUMN directly. Consider alternative approaches such as creating a new table without the column.")
                elif operation == "Execute Custom SQL":
                    cursor.execute(custom_sql)
                    st.success("Custom SQL executed successfully.")
                conn.commit()
                # Push changes to GitHub after schema modifications or other operations
                push_db_to_github(st.secrets["general"]["db_path"])
            except Exception as e:
                st.error(f"Error: {e}")
            finally:
                conn.close()

if __name__ == "__main__":
    main()
