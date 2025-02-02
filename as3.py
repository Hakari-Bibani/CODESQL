import streamlit as st
import os
import sqlite3  # Added for database connection
from grades.grade3 import grade_assignment
from github_sync import push_db_to_github  # Added for GitHub sync

def show():
    st.title("Assignment 3: Advanced Earthquake Data Analysis")

    # Initialize session state variables
    if "assignment4_submitted" not in st.session_state:
        st.session_state["assignment4_submitted"] = False
    if "verified" not in st.session_state:
        st.session_state["verified"] = False
    if "password_entered" not in st.session_state:
        st.session_state["password_entered"] = False

    # Get database path from secrets
    db_path = st.secrets["general"]["db_path"]  # Added database path

    if st.session_state["assignment4_submitted"]:
        st.warning("You cannot resubmit Assignment 3 after submitting Assignment 4.")
        return

    # Modified Step 1: Password Verification instead of Student ID
    st.header("Step 1: Enter Your Password")
    password = st.text_input("Enter Your Password", type="password")
    verify_button = st.button("Verify Password")

    if verify_button and password:
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            # Check password and assignment 4 status
            cursor.execute("SELECT as4 FROM records WHERE password = ?", (password,))
            result = cursor.fetchone()
            
            if result:
                if result[0] != 0:  # Check if Assignment 4 is submitted
                    st.error("You cannot resubmit Assignment 3 after submitting Assignment 4.")
                    st.session_state["verified"] = False
                else:
                    st.success("Password verified. Proceed to the next steps.")
                    st.session_state["verified"] = True
                    st.session_state["password"] = password
            else:
                st.error("Invalid password. Please enter the correct registered password.")
                st.session_state["verified"] = False
                
            conn.close()
        except Exception as e:
            st.error(f"Database error: {e}")

    if st.session_state.get("verified", False):
        # ... (rest of the original code remains the same until submission section)

        # Modified submission section - removed Google Sheets reference
        if submit_button:
            try:
                if not uploaded_html or not uploaded_excel:
                    st.error("Please upload both required files")
                    return

                # Save uploaded files temporarily (original code remains)
                temp_dir = "temp_uploads"
                os.makedirs(temp_dir, exist_ok=True)

                html_path = os.path.join(temp_dir, "uploaded_map.html")
                with open(html_path, "wb") as f:
                    f.write(uploaded_html.getvalue())

                excel_path = os.path.join(temp_dir, "uploaded_sheet.xlsx")
                with open(excel_path, "wb") as f:
                    f.write(uploaded_excel.getvalue())

                # Grade the assignment (original code remains)
                total_grade, grading_breakdown = grade_assignment(code_input, html_path, excel_path)
                st.success(f"Your total grade: {total_grade}/100")

                # Update SQLite database instead of Google Sheets
                try:
                    conn = sqlite3.connect(db_path)
                    cursor = conn.cursor()
                    # Update as3 column for the matching password
                    cursor.execute("UPDATE records SET as3 = ? WHERE password = ?", 
                                 (total_grade, st.session_state["password"]))
                    conn.commit()
                    st.success("Grade saved successfully!")
                    
                    # Push to GitHub
                    push_db_to_github(db_path)
                    
                except Exception as db_error:
                    st.error(f"Database error: {db_error}")
                finally:
                    conn.close()

            except Exception as e:
                st.error(f"Submission error: {e}")

if __name__ == "__main__":
    show()
