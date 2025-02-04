# admin.py
import streamlit as st
import sqlite3
from github_sync import push_db_to_github  # if you want to push changes back to GitHub
import pandas as pd

# Function to run a query (for SELECT statements)
def run_query(query, params=None):
    db_path = st.secrets["general"]["db_path"]
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # for getting dict-like rows
    cursor = conn.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        results = cursor.fetchall()
        conn.commit()
        return results
    except Exception as e:
        st.error(f"Error executing query: {e}")
        return None
    finally:
        conn.close()

# Function to run a non-returning query (like INSERT, UPDATE, DELETE, ALTER TABLE)
def run_non_query(query, params=None):
    db_path = st.secrets["general"]["db_path"]
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
        st.success("Query executed successfully.")
    except Exception as e:
        st.error(f"Error executing query: {e}")
    finally:
        conn.close()

def display_table(table_name):
    query = f"SELECT * FROM {table_name}"
    results = run_query(query)
    if results is not None:
        df = pd.DataFrame(results, columns=results[0].keys() if results else [])
        st.dataframe(df)

def add_row_ui(table_name):
    st.write(f"Adding a new row to {table_name}")
    
    # Fetch the table columns by running a pragma query
    db_path = st.secrets["general"]["db_path"]
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns_info = cursor.fetchall()
    conn.close()
    
    # columns_info: list of tuples (cid, name, type, notnull, dflt_value, pk)
    if not columns_info:
        st.error("Table not found or empty table info.")
        return

    # Build a form dynamically for each column
    with st.form(key="add_row_form"):
        inputs = {}
        for col in columns_info:
            col_name = col[1]
            col_type = col[2].upper()
            # We won’t allow editing of primary key if it's auto-increment (optional)
            # You can customize this logic as needed.
            if col_name == "rowid":  # if using implicit rowid, skip
                continue

            if "INT" in col_type:
                inputs[col_name] = st.number_input(f"{col_name} (Integer)", step=1, format="%d")
            elif "REAL" in col_type or "FLOAT" in col_type:
                inputs[col_name] = st.number_input(f"{col_name} (Real)")
            else:
                inputs[col_name] = st.text_input(f"{col_name} (Text)")
                
        submitted = st.form_submit_button("Add Row")
        if submitted:
            # Build query dynamically. This is a simple example;
            # You may need to handle type conversion and missing values.
            cols = ", ".join(inputs.keys())
            placeholders = ", ".join("?" for _ in inputs)
            values = list(inputs.values())
            insert_query = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
            run_non_query(insert_query, values)
            st.experimental_rerun()

def delete_row_ui(table_name):
    st.write(f"Deleting a row from {table_name}")
    condition = st.text_input("Enter SQL condition (e.g., username = 'john')")
    if st.button("Delete Row"):
        if condition:
            delete_query = f"DELETE FROM {table_name} WHERE {condition}"
            run_non_query(delete_query)
            st.experimental_rerun()
        else:
            st.error("Please provide a condition to delete a row.")

def custom_sql_ui():
    st.write("Execute Custom SQL")
    query = st.text_area("Enter your SQL query")
    if st.button("Execute Query"):
        if query.strip().upper().startswith("SELECT"):
            results = run_query(query)
            if results is not None:
                if results:
                    df = pd.DataFrame(results, columns=results[0].keys())
                    st.dataframe(df)
                else:
                    st.info("Query executed successfully, but returned no results.")
        else:
            run_non_query(query)
            st.info("Query executed (if no error was shown, it was successful).")

def main():
    st.title("Admin Panel")
    
    # --- Authentication ---
    password = st.text_input("Enter admin password:", type="password")
    # You can store the admin password in st.secrets["admin"]["password"]
    if password != st.secrets["admin"]["password"]:
        st.error("Incorrect password")
        return
    st.success("Logged in as admin!")
    
    # --- Admin Operations ---
    option = st.sidebar.selectbox(
        "Choose an action",
        ["View Table", "Add Row", "Delete Row", "Execute Custom SQL"]
    )
    
    if option == "View Table":
        table = st.selectbox("Select table to view", ["users", "records", "admin"])
        display_table(table)
    
    elif option == "Add Row":
        table = st.selectbox("Select table to add a row", ["users", "records", "admin"])
        add_row_ui(table)
    
    elif option == "Delete Row":
        table = st.selectbox("Select table to delete a row from", ["users", "records", "admin"])
        delete_row_ui(table)
    
    elif option == "Execute Custom SQL":
        custom_sql_ui()
    
    # Optionally, after making changes, you could push the updated DB to GitHub.
    if st.button("Push DB to GitHub"):
        db_path = st.secrets["general"]["db_path"]
        push_db_to_github(db_path)

if __name__ == "__main__":
    main()
