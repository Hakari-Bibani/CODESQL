import streamlit as st
import folium
import pandas as pd
from geopy.distance import geodesic
from io import StringIO
from streamlit_folium import st_folium
from utils.style1 import set_page_style
import sqlite3
from github_sync import push_db_to_github

def show():
    # Apply the custom page style
    set_page_style()

    # Initialize session state variables
    if "run_success" not in st.session_state:
        st.session_state["run_success"] = False
    if "map_object" not in st.session_state:
        st.session_state["map_object"] = None
    if "dataframe_object" not in st.session_state:
        st.session_state["dataframe_object"] = None
    if "captured_output" not in st.session_state:
        st.session_state["captured_output"] = ""
    if "password_entered" not in st.session_state:
        st.session_state["password_entered"] = False
    if "valid_password" not in st.session_state:
        st.session_state["valid_password"] = False

    # Define db_path globally
    db_path = st.secrets["general"]["db_path"]

    st.title("Assignment 1: Mapping Coordinates and Calculating Distances")

    # STEP 1: ENTER YOUR PASSWORD
    st.header("Step 1: Enter Your Password")
    password = st.text_input("Password", type="password", key="as1_password")
    enter_password = st.button("Enter")

    if enter_password and password:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM records WHERE password = ?", (password,))
        user_record = cursor.fetchone()

        if user_record:
            if user_record[6] != 0:
                st.error("You have already submitted Assignment 2. Resubmitting Assignment 1 is not allowed.")
            else:
                st.session_state["password_entered"] = True
                st.session_state["valid_password"] = True
        else:
            st.error("Invalid password. Please enter the correct password registered before.")
        conn.close()

    if st.session_state["password_entered"] and st.session_state["valid_password"]:
        # STEP 2: REVIEW ASSIGNMENT DETAILS
        st.header("Step 2: Review Assignment Details")
        tab1, tab2 = st.tabs(["Assignment Details", "Grading Details"])

        with tab1:
            st.markdown("""
            ### Objective
            In this assignment, you will write a Python script to plot three geographical coordinates on a map and calculate the distance between each pair of points in kilometers.
            """)
            with st.expander("See More"):
                st.markdown("""
                **Task Requirements:**
                1. Plot the Three Coordinates on a Map.
                2. Calculate the Distance Between Each Pair of Points.
                """)

        with tab2:
            st.markdown("""
            ### Detailed Grading Breakdown
            #### Code Structure and Implementation (30 points)
            #### Map Visualization (40 points)
            #### Distance Calculations (30 points)
            """)

        # STEP 3: RUN AND SUBMIT YOUR CODE
        st.header("Step 3: Run and Submit Your Code")
        st.markdown('<p style="color: white;">**🖍️ Paste Your Code Here**</p>', unsafe_allow_html=True)
        code_input = st.text_area("", height=300)

        run_button = st.button("Run Code", key="run_code_button")
        if run_button and code_input:
            st.session_state["run_success"] = False
            st.session_state["captured_output"] = ""
            try:
                captured_output = StringIO()
                sys.stdout = captured_output

                local_context = {}
                exec(code_input, {}, local_context)

                sys.stdout = sys.__stdout__
                st.session_state["captured_output"] = captured_output.getvalue()

                map_object = next((obj for obj in local_context.values() if isinstance(obj, folium.Map)), None)
                dataframe_object = next((obj for obj in local_context.values() if isinstance(obj, pd.DataFrame)), None)

                st.session_state["map_object"] = map_object
                st.session_state["dataframe_object"] = dataframe_object

                st.session_state["run_success"] = True

            except Exception as e:
                sys.stdout = sys.__stdout__
                st.error(f"An error occurred while running your code: {e}")

        if st.session_state["run_success"]:
            st.markdown('<p style="color: white;">### 📄 Captured Output</p>', unsafe_allow_html=True)
            if st.session_state["captured_output"]:
                st.text(st.session_state["captured_output"])
            else:
                st.write("No text output captured.")

            if st.session_state["map_object"]:
                st.markdown("### 🖘️ Map Output")
                st_folium(st.session_state["map_object"], width=700, height=500)

            if st.session_state["dataframe_object"] is not None:
                st.markdown("### 📊 DataFrame Output")
                st.dataframe(st.session_state["dataframe_object"])

        submit_button = st.button("Submit Code", key="submit_code_button")
        if submit_button:
            if not st.session_state.get("run_success", False):
                st.error("Please run your code successfully before submitting.")
            elif password:
                from grades.grade1 import grade_assignment
                grade = grade_assignment(code_input)

                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                cursor.execute("UPDATE records SET as1 = ? WHERE password = ?", (grade, password))
                conn.commit()
                conn.close()

                push_db_to_github(db_path)

                st.success(f"Submission successful! Your grade: {grade}/100")
            else:
                st.error("Please enter your password to submit.")
