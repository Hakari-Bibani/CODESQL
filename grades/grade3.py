import pandas as pd

def grade_assignment(code, html_path, excel_path):
    """
    Grades Assignment 3 based on the provided code, HTML file, and Excel file.
    Returns a numerical grade (0-100) with breakdowns.
    """
    total_score = 0
    grading_breakdown = {}

    #### Part 1: Code Grading (45 Points Total) ####

    # Library Imports (15 Points)
    lib_points = 0
    if any(lib in code for lib in ["pandas", "openpyxl"]):  # Updated for Excel handling
        lib_points += 6
    if any(lib in code for lib in ["folium", "plotly", "geopandas"]):
        lib_points += 7
    if "sqlite3" in code:  # Added for database connection
        lib_points += 2
    grading_breakdown["Library Imports"] = lib_points
    total_score += lib_points

    # Code Quality (20 Points)
    quality_points = 0
    # Updated descriptive keywords for password system
    descriptive_keywords = ["password", "temp_dir", "uploaded", "temperature"]
    if any(word in code for word in descriptive_keywords):
        quality_points += 5
    if " = " in code:
        quality_points += 5
    if "#" in code:
        quality_points += 5
    if "def " in code:
        quality_points += 5
    grading_breakdown["Code Quality"] = quality_points
    total_score += quality_points

    # Database Connection Check (5 Points)
    if "sqlite3.connect" in code:
        grading_breakdown["Database Connection"] = 5
        total_score += 5
    else:
        grading_breakdown["Database Connection"] = 0

    # Sheet Creation (10 Points)
    sheet_points = 0
    if "Below_25" in code:
        sheet_points += 5
    if "Above_25" in code:
        sheet_points += 5
    grading_breakdown["Sheet Creation"] = sheet_points
    total_score += sheet_points

    #### Part 2: HTML File Grading (10 Points Total) ####
    html_points = 0
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read().lower()
            if "blue" in html_content:
                html_points += 5
            if "red" in html_content:
                html_points += 5
    except Exception as e:
        print(f"Error reading HTML file: {e}")
    grading_breakdown["HTML File"] = html_points
    total_score += html_points

    #### Part 3: Excel File Grading (30 Points Total) ####
    excel_points = 0
    try:
        uploaded_xl = pd.ExcelFile(excel_path)

        # Correct Sheets (15 Points)
        expected_sheets = ['Sheet1', 'Above_25', 'Below_25']
        uploaded_sheets = [sheet.lower() for sheet in uploaded_xl.sheet_names]
        sheet_points = 0
        for sheet in expected_sheets:
            if sheet.lower() in uploaded_sheets:
                sheet_points += 5
        excel_points += sheet_points
        grading_breakdown["Correct Sheets"] = sheet_points

        # Correct Columns (15 Points)
        expected_columns = ['longitude', 'latitude', 'temperature']
        column_points = 0
        for sheet in expected_sheets:
            if sheet.lower() in uploaded_sheets:
                uploaded_df = uploaded_xl.parse(sheet)
                uploaded_columns = [col.lower() for col in uploaded_df.columns]
                for col in expected_columns:
                    if col.lower() in uploaded_columns:
                        column_points += 5 / len(expected_columns)
        excel_points += column_points
        grading_breakdown["Correct Columns"] = column_points

        # Row Count Validation (10 Points)
        row_points = 0
        if "above_25" in uploaded_sheets:
            uploaded_df = uploaded_xl.parse("Above_25")
            if abs(len(uploaded_df) - 237) <= 3:
                row_points = 10
        excel_points += row_points
        grading_breakdown["Row Count Validation"] = row_points

    except Exception as e:
        print(f"Error processing Excel file: {e}")
    grading_breakdown["Excel File"] = excel_points
    total_score += excel_points

    # Ensure the total score doesn't exceed 100
    return min(total_score, 100), grading_breakdown
