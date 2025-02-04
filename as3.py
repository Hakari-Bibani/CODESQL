import streamlit as st
import os
from grades.grade3 import grade_assignment
import sqlite3
from github_sync import push_db_to_github  # Assuming this is used to sync the database

def show():
    st.title("Assignment 3: Advanced Earthquake Data Analysis")
    
    # Inject CSS to make specific widget labels white
    st.markdown(
        """
        <style>
        .stTextArea label, .stFileUploader label {
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Step 1: Validate Password
    st.markdown('<h1 style="color: #ADD8E6;">Step 1: Enter Your Password</h1>', unsafe_allow_html=True)
    password = st.text_input("Enter Your Password", type="password")
    verify_button = st.button("Verify Password")

    if verify_button and password:
        try:
            db_path = st.secrets["general"]["db_path"]
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM records WHERE password = ?", (password,))
            user_record = cursor.fetchone()

            if user_record:
                # Check if Assignment 4 has been submitted.
                # If as4 is nonzero, then Assignment 4 is already submitted and resubmission for as3 is locked.
                cursor.execute("SELECT as4 FROM records WHERE password = ?", (password,))
                as4_value = cursor.fetchone()[0]
                if as4_value != 0:
                    st.error("Assignment 4 has already been submitted. Resubmitting Assignment 3 is not allowed.")
                    st.session_state["verified"] = False
                else:
                    st.success("Password verified. Proceed to the next steps.")
                    st.session_state["verified"] = True
            else:
                st.error("Invalid password. Please enter a valid, registered password.")
                st.session_state["verified"] = False

            conn.close()

        except Exception as e:
            st.error(f"An error occurred while verifying the password: {e}")
            st.session_state["verified"] = False

    if st.session_state.get("verified", False):
        # Step 2: Review Assignment Details
        st.markdown('<h1 style="color: #ADD8E6;">Step 2: Review Assignment Details</h1>', unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["Assignment Details", "Grading Details"])

        with tab1:
            st.markdown("""
            ### Objective
            In this assignment, students will work with geographical temperature data and apply Python programming to perform data manipulation and visualization. The task is broken into three stages, with each stage encapsulating a specific function. By the end of the assignment, students will merge the functions into one script to complete the task efficiently.
            """)
            with st.expander("See More"):
                st.markdown("""
            ### Stage 1: Filtering Data Below 25°C
            **Goal**: Create a new tab in the spreadsheet containing only the data points where the temperature is below 25°C.
            **Instructions**:
            - Load the provided Excel file containing longitude, latitude, and temperature data.
            - Write a Python script that filters out all the rows where the temperature is below 25°C.
            - Save this filtered data in a new sheet within the same Excel file, naming the new sheet "Below_25".
            **Deliverable**: A script that filters and saves the data in the "Below_25" tab of the Excel file.

            ### Stage 2: Filtering Data Above 25°C
            **Goal**: Create another tab in the spreadsheet containing only the data points where the temperature is above 25°C.
            **Instructions**:
            - Extend your script to filter out all the rows where the temperature is above 25°C.
            - Save this filtered data in a new sheet named "Above_25".
            **Deliverable**: A script that adds the "Above_25" tab to the Excel file.

            ### Stage 3: Visualizing Data on a Map
            **Goal**: Visualize the data points from both the "Below_25" and "Above_25" tabs on a geographical map.
            **Instructions**:
            - Using a Python mapping library (such as folium, matplotlib, or plotly), plot the data points from both the "Below_25" and "Above_25" tabs.
            - Use blue to represent the data points from the "Below_25" tab and red for the "Above_25" tab.
            - Ensure the map accurately displays the temperature data at the correct coordinates.
            **Deliverable**: A Python script that generates a map displaying the data points in blue and red.

            ### Final Task: Merging the Scripts
            **Goal**: Combine all three stages into one cohesive Python script that performs the filtering and visualization tasks in sequence.
            **Instructions**:
            - Encapsulate the functionality of the three scripts (Stage 1, Stage 2, and Stage 3) into distinct functions.
            - Write a master function that calls these functions in sequence:
                1. First, filter the data below 25°C and save it to a new tab.
                2. Then, filter the data above 25°C and save it to another tab.
                3. Finally, visualize both sets of data on a map.
            - Ensure that the final script runs all the steps seamlessly.
            **Deliverable**: A Python script that completes the entire task, from filtering the data to visualizing it on a map.
                """)

        with tab2:
            st.markdown("""
            ### Detailed Grading Breakdown
            #### 1. Library Imports (10 Points)
            - Checks if the required libraries are imported correctly.
            """)
            with st.expander("See More"):
                st.markdown("""
            #### 2. Code Quality (20 Points)
            - **Descriptive Variable Names (5 Points)**:
                - Deducted if non-descriptive variable names are used (e.g., `x`, `y`).
            - **Spacing and Indentation (5 Points)**:
                - Deducted if improper spacing or indentation is found.
            - **Comments (5 Points)**:
                - Deducted if no comments are present to explain major steps.
            - **Code Organization (5 Points)**:
                - Deducted if code blocks are not logically separated with blank lines or functions.

            #### 3. Functionality (10 Points)
            - **JSON API Usage (5 Points)**:
                - Deducted if the JSON API is not used effectively.
            - **Function Encapsulation (5 Points)**:
                - Deducted if the functionality of Stage 1, Stage 2, and Stage 3 is not encapsulated into distinct functions.

            #### 4. Data Filtering (10 Points)
            - **Filter Data Below 25°C (5 Points)**:
                - Deducted if the filtering is incorrect or incomplete.
            - **Filter Data Above 25°C (5 Points)**:
                - Deducted if the filtering is incorrect or incomplete.

            #### 5. Data Mapping and Visualization (20 Points)
            - **Map Generation (5 Points)**:
                - Deducted if the map is not generated or displayed.
            - **Color-Coded Data Points (10 Points)**:
                - Deducted if data points are not color-coded correctly:
                    - Blue for "Below_25": 5 points
                    - Red for "Above_25": 5 points
            - **Accuracy of Coordinates (5 Points)**:
                - Deducted if the map does not accurately display the temperature data at the correct coordinates.

            #### 6. Excel File Grading (30 Points)
            - **Correct Sheets (10 Points)**:
                - Deducted if the Excel file does not include the "Below_25" and "Above_25" sheets.
            - **Data Accuracy (10 Points)**:
                - Deducted if the data in the sheets is incorrect or incomplete.
            - **File Format (10 Points)**:
                - Deducted if the file is not saved in the correct format or structure.
                """)

        # Step 3: Assignment Submission
        st.markdown('<h1 style="color: #ADD8E6;">Step 3: Submit Your Assignment</h1>', unsafe_allow_html=True)
        code_input = st.text_area("**📝 Paste Your Code Here**", height=300)

        # Step 4: Upload Files
        st.markdown('<h1 style="color: #ADD8E6;">Step 4: Upload Your HTML and Excel Files</h1>', unsafe_allow_html=True)
        uploaded_html = st.file_uploader("Upload your HTML file (Map)", type=["html"])
        uploaded_excel = st.file_uploader("Upload your Excel file", type=["xlsx"])

        # Submit Button
        submit_button = st.button("Submit Assignment")

        if submit_button:
            try:
                # Validate required file uploads
                if not uploaded_html:
                    st.error("Please upload an HTML file for the interactive map.")
                    return
                if not uploaded_excel:
                    st.error("Please upload your Excel file.")
                    return

                # Save uploaded files temporarily
                temp_dir = "temp_uploads"
                os.makedirs(temp_dir, exist_ok=True)
                html_path = os.path.join(temp_dir, "uploaded_map.html")
                excel_path = os.path.join(temp_dir, "uploaded_sheet.xlsx")

                with open(html_path, "wb") as f:
                    f.write(uploaded_html.getvalue())
                with open(excel_path, "wb") as f:
                    f.write(uploaded_excel.getvalue())

                # Grade the assignment
                total_grade, grading_breakdown = grade_assignment(code_input, html_path, excel_path)
                st.success(f"Your total grade: {total_grade}/100")

                # Update the grade in the records table (save in as3 column)
                db_path = st.secrets["general"]["db_path"]
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                cursor.execute("UPDATE records SET as3 = ? WHERE password = ?", (total_grade, password))
                conn.commit()
                conn.close()

                # Push the updated DB to GitHub
                push_db_to_github(db_path)

            except Exception as e:
                st.error(f"An error occurred during submission: {e}")

if __name__ == "__main__":
    show()
