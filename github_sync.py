import sqlite3
import streamlit as st
import time
from github_sync import push_db_to_github  # Use the simple version you shared

def update_grade_and_push(db_path, username, new_grade):
    """
    Update the grade in the records table and push the updated DB file to GitHub.
    """
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Ensure that the record exists by checking current grade for the username
    cursor.execute("SELECT as1 FROM records WHERE username = ?", (username,))
    row = cursor.fetchone()
    if row is None:
        st.error(f"No record found for username '{username}'.")
        conn.close()
        return
    else:
        st.info(f"Current grade for {username}: {row[0]}")

    # Update the grade in the records table
    cursor.execute("UPDATE records SET as1 = ? WHERE username = ?", (new_grade, username))
    conn.commit()
    st.info(f"Rows updated: {cursor.rowcount}")

    # Verify that the update took place
    cursor.execute("SELECT as1 FROM records WHERE username = ?", (username,))
    updated = cursor.fetchone()
    conn.close()

    if updated:
        st.info(f"New grade for {username} in local DB: {updated[0]}")
    else:
        st.error("Update failed!")

    # Wait briefly to ensure the file is flushed to disk
    time.sleep(1)

    # Push the updated DB file to GitHub
    push_db_to_github(db_path)

# Example usage in your app's submission handler:
db_path = st.secrets["general"]["db_path"]  # e.g., "mydatabase.db"
username = st.session_state.get("username", "").strip()  # Ensure no extra spaces
# Assume you get the new grade from your grade_assignment() function
new_grade = 98.0  # Replace with your actual calculated grade

if username:
    update_grade_and_push(db_path, username, new_grade)
else:
    st.error("Username not provided. Cannot update grade.")
