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

    # ────────────────────────────────────────────────────────
    # STEP 1: ENTER YOUR PASSWORD
    # ────────────────────────────────────────────────────────
    st.markdown('<h2 style="color: blue;">Step 1: Enter Your Password</h2>', unsafe_allow_html=True)
    password = st.text_input("Password", type="password", key="as1_password")
    enter_password = st.button("Enter")

    if enter_password and password:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM records WHERE password = ?", (password,))
        user_record = cursor.fetchone()

        if user_record:
            # Check if Assignment 2 has already been submitted
            if user_record[6] != 0:  # Assuming as2 is the 7th column (index 6)
                st.error("You have already submitted Assignment 2. Resubmitting Assignment 1 is not allowed.")
            else:
                st.session_state["password_entered"] = True
                st.session_state["valid_password"] = True
        else:
            st.error("Invalid password. Please enter the correct password registered before.")
        conn.close()

    if st.session_state["password_entered"] and st.session_state["valid_password"]:
        # ────────────────────────────────────────────────────────
        # STEP 2: REVIEW ASSIGNMENT DETAILS
        # ────────────────────────────────────────────────────────
        st.markdown('<h2 style="color: blue;">Step 2: Review Assignment Details</h2>', unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["Assignment Details", "Grading Details"])

        with tab1:
            st.markdown("""
            ### Objective
            In this assignment, you will write a Python script to plot three geographical coordinates on a map and calculate the distance between each pair of points in kilometers. This will help you practice working with geospatial data and Python libraries for mapping and calculations.

            ### Assignment: Week 1 – Mapping Coordinates and Calculating Distances in Python
            **Objective:**
            In this assignment, you will write a Python script to plot three geographical coordinates on a map and calculate the distance between each pair of points in kilometers. This will help you practice working with geospatial data and Python libraries for mapping and calculations.
            """)
            with st.expander("See More"):
                st.markdown("""
            **Task Requirements:**
            1. **Plot the Three Coordinates on a Map:**
               - The coordinates represent three locations in the Kurdistan Region.
               - You will use Python libraries to plot these points on a map.
               - The map should visually display the exact locations of the coordinates.
            2. **Calculate the Distance Between Each Pair of Points:**
               - You will calculate the distances between the three points in kilometers.
               - Specifically, calculate:
                 - The distance between Point 1 and Point 2.
                 - The distance between Point 2 and Point 3.
                 - The distance between Point 1 and Point 3.
               - Add Markers to the map for each coordinate.
               - Add polylines to connect the points.
               - Add popups to display information about the distance.

            **Coordinates:**
            - Point 1: Latitude: 36.325735, Longitude: 43.928414
            - Point 2: Latitude: 36.393432, Longitude: 44.586781
            - Point 3: Latitude: 36.660477, Longitude: 43.840174

            **Python Libraries You Will Use:**
            - geopy for calculating the distance between two coordinates.
            - folium for plotting the points on an interactive map.
            - pandas to create a DataFrame that displays the distances between the points.

            **Expected Output:**
            1. A map showing the three coordinates.
            2. A text summary (Express values to two decimal places.): showing the calculated distances (in kilometers) between:
               - Point 1 and Point 2.
               - Point 2 and Point 3.
               - Point 1 and Point 3.
            """)

        with tab2:
            st.markdown("""
            ### Detailed Grading Breakdown
            #### 1. Code Structure and Implementation (30 points)
            - **Library Imports (5 points):**
                - Checks if the required libraries (folium, geopy, geodesic) are imported.
            - **Coordinate Handling (5 points):**
                - Checks if the correct coordinates are defined in the code.
            - **Code Execution (10 points):**
                - Checks if the code runs without errors.
            - **Code Quality (10 points):**
                - **Variable Naming:** 2 points (deducted if single-letter variables are used).
                - **Spacing:** 2 points (deducted if improper spacing is found, e.g., no space after =).
                - **Comments:** 2 points (deducted if no comments are present).
                - **Code Organization:** 2 points (deducted if no blank lines are used for separation).
            """)
            with st.expander("See More"):
                st.markdown("""
            #### 2. Map Visualization (40 points)
            - **Map Generation (15 points):**
                - Checks if the folium.Map is correctly initialized.
            - **Markers (15 points):**
                - Checks if markers are added to the map for each coordinate.
            - **Polylines (5 points):**
                - Checks if polylines are used to connect the points.
            - **Popups (5 points):**
                - Checks if popups are added to the markers.

            #### 3. Distance Calculations (30 points)
            - **Geodesic Implementation (10 points):**
                - Checks if the geodesic function is used correctly to calculate distances.
            - **Distance Accuracy (20 points):**
                - Checks if the calculated distances are accurate within a 100-meter tolerance.
            """)

        # ────────────────────────────────────────────────────────
        # STEP 3: RUN AND SUBMIT YOUR CODE
        # ────────────────────────────────────────────────────────
        st.markdown('<h2 style="color: blue;">Step 3: Run and Submit Your Code</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color: white;">🖍️ Paste Your Code Here</p>', unsafe_allow_html=True)
        code_input = st.text_area("", height=300)  # Removed label since we're using custom markdown above
