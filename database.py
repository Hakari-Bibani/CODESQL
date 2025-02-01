# database.py
import sqlite3
import streamlit as st
import os
from github_sync import pull_db_from_github

def create_tables():
    """Create the required tables in the database if they don't exist."""
    db_path = st.secrets["general"]["db_path"]

    # 1) Pull the DB from GitHub to ensure local is updated
    pull_db_from_github(db_path)

    # 2) Now proceed with table creation
    conn = sqlite3.connect(db_path)
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
