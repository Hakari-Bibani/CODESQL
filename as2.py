# as2.py - Adapted for password-based login and database storage
import streamlit as st
import os
from grades.grade2 import grade_assignment  # ensure this path is correct in your project
from database import create_tables
import sqlite3
from github_sync import push_db_to_github

def update_grade_in_db(password, grade):
    db_path = st.secrets["general"]["db_path"]
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE records
        SET as2 = ?
        WHERE password = ?
    """, (grade, password))
    conn.commit()
    conn.close()
    push_db_to_github(db_path)

def show():
    apply_custom_styles()  # Applying consistent styles
    st.title("Assignment 2: Earthquake Data Analysis")

    # Step 1: Validate User Password
    st.header("Step 1: Enter Your Password")
    password = st.text_input("Enter Your Password", type="password")
    verify_button = st.button("Verify Password")

    if verify_button:
        db_path = st.secrets["general"]["db_path"]
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE password = ?", (password,))
        user_data = cursor.fetchone()
        conn.close()

        if user_data:
            st.success(f"Password verified. Welcome, {user_data[0]}!")
            st.session_state["verified"] = True
        else:
            st.error("Invalid password. Please enter a valid registered password.")
            st.session_state["verified"] = False

    if st.session_state.get("verified", False):
        # Step 2: Assignment and Grading Details
        st.header("Step 2: Review Assignment Details")
        tab1, tab2 = st.tabs(["Assignment Details", "Grading Details"])

        with tab1:
            st.markdown("""
            ### Objective
            In this assignment, you will write a Python script that fetches real-time earthquake data from the USGS Earthquake API, processes the data to filter earthquakes with a magnitude greater than 4.0, and plots the earthquake locations on a map.
            """)
            with st.expander("See More"):
                st.markdown("""
                ### Task Requirements
                - **Fetch Earthquake Data**: Use the USGS Earthquake API for the date range **January 2nd, 2025, to January 9th, 2025**.
                - **Filter Data**: Only include earthquakes with magnitude > 4.0.
                - **Map Visualization**: Create an interactive map using `folium`.
                - **Bar Chart**: Visualize earthquake frequency by magnitude.
                - **Text Summary**: Generate a CSV with total earthquakes and magnitude statistics.
                """)

        with tab2:
            st.markdown("""
            ### Detailed Grading Breakdown
            #### 1. Library Imports (10 Points)
            - Checks if the required libraries (`folium`, `matplotlib`, `requests`, `pandas`) are imported.
            """)
            with st.expander("See More"):
                st.markdown("""
                #### 2. Code Quality (20 Points)
                - **Variable Naming (5 Points)**
                - **Spacing (5 Points)**
                - **Comments (5 Points)**
                - **Code Organization (5 Points)**
                #### 3. Fetching Data from the API (10 Points)
                - **Correct API URL (5 Points)**
                - **Successful Data Retrieval (5 Points)**
                """)

        # Step 3: Code Submission and Output
        st.header("Step 3: Run and Submit Your Code")
        code_input = st.text_area("**📝 Paste Your Code Here**", height=300)

        # Step 4: Upload Files
        st.header("Step 4: Upload Your Outputs")
        uploaded_html = st.file_uploader("Upload your HTML file (Map)", type=["html"])
        uploaded_png = st.file_uploader("Upload your PNG file (Bar Chart)", type=["png"])
        uploaded_csv = st.file_uploader("Upload your CSV file (Summary)", type=["csv"])

        all_uploaded = all([uploaded_html, uploaded_png, uploaded_csv])
        st.write("All files uploaded:", "✅ Yes" if all_uploaded else "❌ No")

        if all_uploaded:
            submit_button = st.button("Submit Assignment")

            if submit_button:
                try:
                    temp_dir = "temp_uploads"
                    os.makedirs(temp_dir, exist_ok=True)
                    html_path = os.path.join(temp_dir, "uploaded_map.html")
                    png_path = os.path.join(temp_dir, "uploaded_chart.png")
                    csv_path = os.path.join(temp_dir, "uploaded_summary.csv")

                    with open(html_path, "wb") as f:
                        f.write(uploaded_html.getvalue())
                    with open(png_path, "wb") as f:
                        f.write(uploaded_png.getvalue())
                    with open(csv_path, "wb") as f:
                        f.write(uploaded_csv.getvalue())

                    # Grade the assignment
                    grade = grade_assignment(code_input, html_path, png_path, csv_path)
                    st.success(f"Your grade for Assignment 2: {grade}/100")

                    # Update the grade in the SQLite database
                    update_grade_in_db(password, grade)
                    st.success("Your grade has been saved in the system.")

                except Exception as e:
                    st.error(f"An error occurred during submission: {e}")

        else:
            st.warning("Please upload all required files to proceed.")

if __name__ == "__main__":
    show()




