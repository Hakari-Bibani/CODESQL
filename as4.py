import streamlit as st
import os
from grades.grade4 import grade_assignment
import sqlite3
from github_sync import push_db_to_github  # Used to sync the updated database

def show():
    st.title("Assignment 4: Image Analysis and Rectangle Detection")

    # Prevent resubmission of Assignment 4 after submitting the next assignment (Assignment 5)
    if "assignment5_submitted" not in st.session_state:
        st.session_state["assignment5_submitted"] = False

    if st.session_state["assignment5_submitted"]:
        st.warning("You cannot resubmit Assignment 4 after submitting the next assignment.")
        return

    # Step 1: Validate Password (instead of Student ID)
    st.markdown("<h2 style='color:#ADD8E6;'>Step 1: Enter Your Password</h2>", unsafe_allow_html=True)
    password = st.text_input("Enter Your Password", type="password")
    verify_button = st.button("Verify Password")

    if verify_button and password:
        try:
            # Connect to the SQLite database
            db_path = st.secrets["general"]["db_path"]
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM records WHERE password = ?", (password,))
            user_record = cursor.fetchone()
            conn.close()

            if user_record:
                st.success("Password verified. Proceed to the next steps.")
                st.session_state["verified"] = True
            else:
                st.error("Invalid password. Please use the password registered previously.")
                st.session_state["verified"] = False

        except Exception as e:
            st.error(f"An error occurred while verifying your password: {e}")
            st.session_state["verified"] = False

    if st.session_state.get("verified", False):
        # Step 2: Review Assignment Details
        st.markdown("<h2 style='color:#ADD8E6;'>Step 2: Review Assignment Details</h2>", unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["Assignment Details", "Grading Details"])

        with tab1:
            st.markdown("""
            ### Objective:
            In this assignment, you will use Python image processing libraries to analyze a black-and-white image, detect rectangular shapes, and determine the coordinates of each rectangle.
            """)
            with st.expander("See More"):
                st.markdown("""
                #### Instructions:
                1. **Set Up Your Environment:**
                   - Open a new Google Colab notebook.
                   - Import the necessary libraries:
                     - `cv2` (OpenCV) for image processing.
                     - `numpy` for numerical operations.
                     - `matplotlib` for displaying images.

                2. **Load the Image:**
                   - Download the provided image and upload it to Google Colab.
                   - Load the image using OpenCV.

                3. **Convert the Image to Grayscale and Apply Thresholding:**
                   - Convert the image to grayscale.
                   - Use binary thresholding to make it easier to detect the rectangular shapes. This will turn the rectangles into clear white shapes against a black background.

                4. **Detect Contours:**
                   - Use OpenCV’s `findContours` function to detect all contours in the image.
                   - Filter out contours that are not rectangular shapes.

                5. **Filter and Identify Rectangles:**
                   - For each contour, approximate its shape using `cv2.approxPolyDP`.
                   - If the contour has four points, consider it a rectangle.
                   - Calculate the bounding box coordinates of each rectangle using `cv2.boundingRect`.

                6. **Extract and Print the Coordinates:**
                   - For each detected rectangle, print the top-left and bottom-right coordinates.
                   - Display the original image with the rectangles outlined for verification.
                """)

        with tab2:
            st.markdown("""
            ### Detailed Grading Breakdown
            """)
            with st.expander("See More"):
                st.markdown("""
                1. **Library Imports (20 Points)**
                   - Checks if the required libraries are imported correctly.

                2. **Code Quality (20 Points)**
                   - **Descriptive Variable Names (5 Points):**
                     - Deducted if non-descriptive variable names are used.
                   - **Spacing and Indentation (5 Points):**
                     - Deducted if improper spacing or indentation is found.
                   - **Comments (5 Points):**
                     - Deducted if no comments are present.
                   - **Code Organization (5 Points):**
                     - Deducted if code blocks are not logically separated.

                3. **Rectangle Coordinates (30 Points)**
                   - Evaluates the extracted rectangle coordinates.

                4. **Thresholded Image (15 Points)**
                   - Evaluates the uploaded thresholded image.

                5. **Image with Rectangles Outlined (15 Points)**
                   - Evaluates the uploaded image with the detected rectangles.
                """)

        # Step 3: Assignment Submission
        st.markdown("<h2 style='color:#ADD8E6;'>Step 3: Submit Your Assignment</h2>", unsafe_allow_html=True)

        # Code Input
        st.markdown("<p style='color:white; font-weight:bold;'>📝 Paste Your Code Here</p>", unsafe_allow_html=True)
        code_input = st.text_area("", height=300)

        # Step 4: Enter Rectangle Coordinates
        st.markdown("<h2 style='color:#ADD8E6;'>Step 4: Enter Rectangle Coordinates</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color:white;'>Paste Rectangle Coordinates (Top-Left and Bottom-Right) Here</p>", unsafe_allow_html=True)
        rectangle_coordinates = st.text_area("", height=150)

        # Step 5: Upload Thresholded Image
        st.markdown("<h2 style='color:#ADD8E6;'>Step 5: Upload Your Thresholded Image</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color:white;'>Upload your thresholded image file</p>", unsafe_allow_html=True)
        uploaded_thresholded_image = st.file_uploader("", type=["png", "jpg", "jpeg"], key="file_uploader_thresholded")

        # Step 6: Upload Image with Rectangles Outlined
        st.markdown("<h2 style='color:#ADD8E6;'>Step 6: Upload Image with Rectangles Outlined</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color:white;'>Upload your image with rectangles outlined</p>", unsafe_allow_html=True)
        uploaded_outlined_image = st.file_uploader("", type=["png", "jpg", "jpeg"], key="file_uploader_outlined")

        # Submit Button
        submit_button = st.button("Submit Assignment")

        if submit_button:
            try:
                # Validate required files
                if not uploaded_thresholded_image:
                    st.error("Please upload a thresholded image file.")
                    return
                if not uploaded_outlined_image:
                    st.error("Please upload an image with rectangles outlined.")
                    return

                # Save uploaded files temporarily
                temp_dir = "temp_uploads"
                os.makedirs(temp_dir, exist_ok=True)

                # Save thresholded image
                thresholded_image_path = os.path.join(temp_dir, "thresholded_image.png")
                with open(thresholded_image_path, "wb") as f:
                    f.write(uploaded_thresholded_image.getvalue())

                # Save outlined image
                outlined_image_path = os.path.join(temp_dir, "outlined_image.png")
                with open(outlined_image_path, "wb") as f:
                    f.write(uploaded_outlined_image.getvalue())

                # Parse rectangle coordinates (the grading logic remains unchanged)
                try:
                    correct_values = [
                        1655, 1305, 2021, 1512, 459, 1305, 825, 1512,
                        2051, 1305, 2417, 1512, 1257, 1305, 1623, 1512,
                        857, 1305, 1223, 1512, 63, 1305, 429, 1512,
                        157, 1050, 398, 1122, 351, 869, 592, 941,
                        624, 744, 865, 816, 888, 646, 1129, 718,
                        1069, 492, 1311, 564, 1338, 360, 1579, 432,
                        64, 231, 800, 506, 2103, 166, 2344, 239
                    ]
                    student_values = [
                        int(value) for line in rectangle_coordinates.splitlines()
                        for value in line.replace("Top-Left (", "").replace("Bottom-Right (", "")
                        .replace(")", "").replace(",", " ").split()
                        if value.isdigit()
                    ]
                    rectangle_grade = sum(1 for i, val in enumerate(student_values) if i < len(correct_values) and val == correct_values[i])
                except Exception as e:
                    st.error(f"Invalid input format for rectangle coordinates: {e}")
                    return

                # Grade Thresholded Image
                thresholded_image_grade = 0
                try:
                    from PIL import Image
                    image = Image.open(thresholded_image_path).convert("L")  # Convert to grayscale
                    if image:
                        thresholded_image_grade = 5  # Award 5 points for a valid black-and-white image
                except Exception as e:
                    st.error(f"Error processing thresholded image: {e}")

                # Grade Outlined Image
                outlined_image_grade = 0
                try:
                    # Simplified check for outlined image validation (assume correct if file exists)
                    outlined_image_grade = 5
                except Exception as e:
                    st.error(f"Error processing outlined image: {e}")

                # Grade the assignment
                total_grade, grading_breakdown = grade_assignment(
                    code_input,
                    rectangle_grade,
                    thresholded_image_grade,
                    outlined_image_grade
                )

                # Display total grade and detailed breakdown
                st.success(f"Your total grade: {total_grade}/100")

                # Update the grade in the records table (save in as4 column) using the entered password
                db_path = st.secrets["general"]["db_path"]
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                cursor.execute("UPDATE records SET as4 = ? WHERE password = ?", (total_grade, password))
                conn.commit()
                conn.close()

                # Push the updated DB to GitHub
                push_db_to_github(db_path)

            except Exception as e:
                st.error(f"An error occurred during submission: {e}")

if __name__ == "__main__":
    show()
