import streamlit as st
import folium
import pandas as pd
from geopy.distance import geodesic
from io import StringIO
from streamlit_folium import st_folium
from utils.style1 import set_page_style
import sqlite3
from github_sync import push_db_to_github
from grades.grade1 import grade_assignment


def show():
    # Apply the custom page style
    set_page_style()

    # Initialize session state variables
    initialize_session_state()

    # Define db_path globally
    db_path = st.secrets["general"]["db_path"]

    st.title("Assignment 1: Mapping Coordinates and Calculating Distances")

    # Step 1: Password Entry
    handle_password_entry(db_path)

    if st.session_state["password_entered"] and st.session_state["valid_password"]:
        # Step 2: Review Assignment Details
        show_assignment_details()

        # Step 3: Run and Submit Your Code
        handle_code_submission(db_path)


def initialize_session_state():
    session_vars = [
        "run_success", "map_object", "dataframe_object",
        "captured_output", "password_entered", "valid_password"
    ]
    for var in session_vars:
        if var not in st.session_state:
            st.session_state[var] = False if "success" in var or "valid" in var else None


def handle_password_entry(db_path):
    st.header("Step 1: Enter Your Password")
    password = st.text_input("Password", type="password", key="as1_password")
    enter_password = st.button("Enter")

    if enter_password and password:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM records WHERE password = ?", (password,))
        user_record = cursor.fetchone()

        if user_record:
            if user_record[6] != 0:  # Check if Assignment 2 is submitted
                st.error("You have already submitted Assignment 2. Resubmitting Assignment 1 is not allowed.")
            else:
                st.session_state["password_entered"] = True
                st.session_state["valid_password"] = True
        else:
            st.error("Invalid password. Please enter the correct password registered before.")
        conn.close()


def show_assignment_details():
    st.header("Step 2: Review Assignment Details")
    tab1, tab2 = st.tabs(["Assignment Details", "Grading Details"])

    with tab1:
        display_assignment_description()

    with tab2:
        display_grading_details()


def display_assignment_description():
    st.markdown("""
    ### Objective
    In this assignment, you will write a Python script to plot three geographical coordinates on a map and calculate the distance between each pair of points in kilometers.
    """)
    with st.expander("See More"):
        st.markdown("""
        **Task Requirements:**
        1. **Plot the Three Coordinates on a Map:**
           - The coordinates represent three locations in the Kurdistan Region.
        2. **Calculate the Distance Between Each Pair of Points:**
           - Specifically, calculate:
             - The distance between Point 1 and Point 2.
             - The distance between Point 2 and Point 3.
             - The distance between Point 1 and Point 3.
        
        **Coordinates:**
        - Point 1: Latitude: 36.325735, Longitude: 43.928414
        - Point 2: Latitude: 36.393432, Longitude: 44.586781
        - Point 3: Latitude: 36.660477, Longitude: 43.840174
        """)


def display_grading_details():
    st.markdown("""
    ### Detailed Grading Breakdown
    #### 1. Code Structure and Implementation (30 points)
    - **Library Imports (5 points)**
    - **Coordinate Handling (5 points)**
    - **Code Execution (10 points)**
    - **Code Quality (10 points)**
    """)
    with st.expander("See More"):
        st.markdown("""
        #### 2. Map Visualization (40 points)
        - **Map Generation (15 points)**
        - **Markers (15 points)**
        - **Polylines (5 points)**
        - **Popups (5 points)**

        #### 3. Distance Calculations (30 points)
        - **Geodesic Implementation (10 points)**
        - **Distance Accuracy (20 points)**
        """)


def handle_code_submission(db_path):
    st.header("Step 3: Run and Submit Your Code")
    code_input = st.text_area("**📝 Paste Your Code Here**", height=300)

    if st.button("Run Code", key="run_code_button") and code_input:
        execute_user_code(code_input)

    display_code_outputs()

    if st.button("Submit Code", key="submit_code_button"):
        submit_user_code(db_path, code_input)


def execute_user_code(code_input):
    st.session_state["run_success"] = False
    st.session_state["captured_output"] = ""
    try:
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output

        local_context = {}
        exec(code_input, {}, local_context)

        sys.stdout = sys.__stdout__
        st.session_state["captured_output"] = captured_output.getvalue()
        st.session_state["map_object"] = next((obj for obj in local_context.values() if isinstance(obj, folium.Map)), None)
        st.session_state["dataframe_object"] = next((obj for obj in local_context.values() if isinstance(obj, pd.DataFrame)), None)
        st.session_state["run_success"] = True

    except Exception as e:
        sys.stdout = sys.__stdout__
        st.error(f"An error occurred while running your code: {e}")


def display_code_outputs():
    if st.session_state["run_success"]:
        st.markdown("### 📄 Captured Output")
        st.text(st.session_state["captured_output"] or "No text output captured.")

        if st.session_state["map_object"]:
            st.markdown("### 🗘️ Map Output")
            st_folium(st.session_state["map_object"], width=1000, height=500)

        if st.session_state["dataframe_object"] is not None:
            st.markdown("### 📊 DataFrame Output")
            st.dataframe(st.session_state["dataframe_object"])


def submit_user_code(db_path, code_input):
    if not st.session_state.get("run_success", False):
        st.error("Please run your code successfully before submitting.")
    elif st.session_state.get("as1_password"):
        grade = grade_assignment(code_input)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE records SET as1 = ? WHERE password = ?", (grade, st.session_state["as1_password"]))
        conn.commit()
        conn.close()

        push_db_to_github(db_path)
        st.success(f"Submission successful! Your grade: {grade}/100")
    else:
        st.error("Please enter your password to submit.")
