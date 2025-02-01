import sqlite3
import streamlit as st

def create_tables():
    """Create the required tables in the database if they don't exist."""
    conn = sqlite3.connect(st.secrets["general"]["db_path"])
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            fullname TEXT,
            email TEXT,
            phone INTEGER,
            username TEXT UNIQUE,
            password TEXT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS records (
            password TEXT,
            fullname TEXT,
            email TEXT,
            as1 REAL,
            as2 REAL,
            as3 REAL,
            as4 REAL,
            quiz1 REAL,
            quiz2 REAL,
            total REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admin (
            fullname TEXT,
            email TEXT,
            phone INTEGER,
            username TEXT,
            password TEXT,
            total REAL
        )
    """)

    conn.commit()
    conn.close()

def save_grade(password, grade, assignment):
    """
    Save the grade in the 'records' table for the given assignment.
    :param password: The password used to identify the user.
    :param grade: The grade to be saved.
    :param assignment: The assignment column (e.g., 'as2') to update.
    """
    db_path = st.secrets["general"]["db_path"]
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Ensure assignment column exists
    if assignment not in ['as1', 'as2', 'as3', 'as4', 'quiz1', 'quiz2']:
        conn.close()
        raise ValueError("Invalid assignment column.")

    try:
        # Update the grade in the specified assignment column
        cursor.execute(f"""
            UPDATE records
            SET {assignment} = ?
            WHERE password = ?
        """, (grade, password))

        conn.commit()
        conn.close()
        print(f"Grade for {assignment} saved successfully.")
    except Exception as e:
        conn.close()
        raise e
