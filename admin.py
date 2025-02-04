# admin.py
import streamlit as st
import sqlite3
from github_sync import push_db_to_github

# Function to get a connection to your SQLite database.
def get_connection():
    db_path = st.secrets["general"]["db_path"]
    conn = sqlite3.connect(db_path)
    return conn

# Admin login function
def admin_login():
    if "admin_logged_in" not in st.session_state:
        st.session_state["admin_logged_in"] = False

    if not st.session_state["admin_logged_in"]:
        st.title("Admin Login")
        username = st.text_input("Admin Username")
        password = st.text_input("Admin Password", type="password")
        if st.button("Login"):
            # Check credentials against st.secrets
            if (username == st.secrets["admin"]["username"] and
                    password == st.secrets["admin"]["password"]):
                st.session_state["admin_logged_in"] = True
                st.success("Logged in as admin!")
            else:
                st.error("Invalid credentials. Please try again.")

    return st.session_state["admin_logged_in"]

# Function to push local database changes to GitHub
def push_changes():
    db_path = st.secrets["general"]["db_path"]
    push_db_to_github(db_path)
    st.success("Database pushed to GitHub successfully.")

# Main admin interface
if admin_login():
    st.title("Admin Dashboard")
    st.write("Use this dashboard to modify your database structure and data.")
    
    # Choose an operation
    operation = st.selectbox(
        "Select Operation",
        [
            "Execute SQL Command",
            "Insert Row",
            "Delete Row",
            "Add Column",
            "Show Table Data"
        ]
    )

    # Option 1: Execute arbitrary SQL commands.
    if operation == "Execute SQL Command":
        st.subheader("Execute Arbitrary SQL")
        st.info("⚠️ Use this with caution. Any valid SQL command can be executed.")
        sql_command = st.text_area("Enter SQL command")
        if st.button("Execute"):
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(sql_command)
                conn.commit()
                st.success("SQL executed successfully.")
                # If it was a SELECT query, display results.
                if sql_command.strip().lower().startswith("select"):
                    results = cursor.fetchall()
                    st.write("Results:", results)
            except Exception as e:
                st.error(f"Error executing SQL: {e}")
            finally:
                conn.close()
        if st.button("Push changes to GitHub"):
            push_changes()

    # Option 2: Insert a new row into a table.
    elif operation == "Insert Row":
        st.subheader("Insert Row into Table")
        table = st.selectbox("Select Table", ["users", "records", "admin"])
        # Retrieve table schema (column names) dynamically.
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA table_info({table})")
            columns_info = cursor.fetchall()  # (cid, name, type, notnull, dflt_value, pk)
            col_names = [col[1] for col in columns_info]
            st.write("Table Columns:", col_names)
        except Exception as e:
            st.error(f"Error fetching table info: {e}")
            conn.close()
        new_data = {}
        for col in col_names:
            new_data[col] = st.text_input(f"Enter value for '{col}'", key=col)
        if st.button("Insert Row"):
            try:
                conn = get_connection()
                cursor = conn.cursor()
                placeholders = ", ".join(["?"] * len(col_names))
                col_names_str = ", ".join(col_names)
                values = [new_data[col] for col in col_names]
                cursor.execute(
                    f"INSERT INTO {table} ({col_names_str}) VALUES ({placeholders})",
                    values
                )
                conn.commit()
                st.success("Row inserted successfully.")
            except Exception as e:
                st.error(f"Error inserting row: {e}")
            finally:
                conn.close()
        if st.button("Push changes to GitHub"):
            push_changes()

    # Option 3: Delete rows from a table based on a WHERE clause.
    elif operation == "Delete Row":
        st.subheader("Delete Row(s) from Table")
        table = st.selectbox("Select Table for Deletion", ["users", "records", "admin"])
        st.write("Provide a WHERE clause to identify rows to delete. For example: username = 'john'")
        where_clause = st.text_input("WHERE clause (without 'WHERE')")
        if st.button("Delete Row(s)"):
            if where_clause.strip() == "":
                st.error("WHERE clause cannot be empty.")
            else:
                try:
                    conn = get_connection()
                    cursor = conn.cursor()
                    query = f"DELETE FROM {table} WHERE {where_clause}"
                    cursor.execute(query)
                    conn.commit()
                    st.success("Row(s) deleted successfully.")
                except Exception as e:
                    st.error(f"Error deleting row(s): {e}")
                finally:
                    conn.close()
        if st.button("Push changes to GitHub"):
            push_changes()

    # Option 4: Add a new column to a table.
    elif operation == "Add Column":
        st.subheader("Add Column to Table")
        table = st.selectbox("Select Table to Alter", ["users", "records", "admin"])
        new_column = st.text_input("New Column Name")
        new_type = st.selectbox("Data Type", ["TEXT", "INTEGER", "REAL", "BLOB"])
        if st.button("Add Column"):
            try:
                conn = get_connection()
                cursor = conn.cursor()
                query = f"ALTER TABLE {table} ADD COLUMN {new_column} {new_type}"
                cursor.execute(query)
                conn.commit()
                st.success(f"Column '{new_column}' added successfully to {table}.")
            except Exception as e:
                st.error(f"Error adding column: {e}")
            finally:
                conn.close()
        if st.button("Push changes to GitHub"):
            push_changes()

    # Option 5: Display table data.
    elif operation == "Show Table Data":
        st.subheader("Display Table Data")
        table = st.selectbox("Select Table to View", ["users", "records", "admin"])
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {table}")
            rows = cursor.fetchall()
            st.write(f"Data from table '{table}':")
            st.write(rows)
        except Exception as e:
            st.error(f"Error fetching data: {e}")
        finally:
            conn.close()
